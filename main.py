import pickle
import time
from constants import SHOP_LIST

from multiprocessing import Pool
from selenium.webdriver.common.by import By
from fake_useragent import UserAgent
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium_stealth import stealth
from webdriver_manager.chrome import ChromeDriverManager

from db.crud import create
from db.models import Category


start_time = time.time()

ua = UserAgent()

options = webdriver.ChromeOptions()
options.add_argument(f"user-agent={ua.random}")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument("--headless")

key_list = list(SHOP_LIST.keys())
val_list = list(SHOP_LIST.values())

def get_category_list(url):
    driver = webdriver.Chrome(
        options=options,
        service=Service(ChromeDriverManager().install())
    )

    stealth(driver,
            languages=["ru-Ru", "ru"],
            vendor="Google Inc.",
            platform="Win32",
            webgl_vendor="Intel Inc.",
            renderer="Intel Iris OpenGL Engine",
            fix_hairline=True,
            )

    try:
        driver.get(url)

        # --- load cookie ---
        for cookie in pickle.load(open(f"cookies", "rb")):
            driver.add_cookie(cookie)
        time.sleep(1)
        driver.refresh()
        time.sleep(1)

        driver.find_element(By.XPATH, '//*[@id="__next"]/div[2]/header/div/div[3]/div/div/div[2]/button[2]').click()
        time.sleep(2)

        list = driver.find_elements(By.CLASS_NAME, 'CategoriesMenuListTitle_styles_root__IKPWK')
        for l in list:
            create(Category, {
                "shop": key_list[val_list.index(url)],
                "name": l.get_attribute('innerHTML'),
            })

    except Exception as e:
        print(e)
    finally:
        driver.quit()
        print(f"Time: {time.time() - start_time}")

if __name__ == '__main__':
    pool = Pool(processes=len(SHOP_LIST))
    pool.map(get_category_list, val_list)

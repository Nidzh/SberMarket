import pickle
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from fake_useragent import UserAgent
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium_stealth import stealth
from webdriver_manager.chrome import ChromeDriverManager

start_time = time.time()

ua = UserAgent()

options = webdriver.ChromeOptions()
options.add_argument(f"user-agent={ua.random}")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
# options.add_argument("--headless")

# --- set proxy ---
# options.add_argument("--proxy-server=138.128.91.65:8000")

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
    url = "https://sbermarket.ru/lenta/"
    driver.get(url)

    # --- load cookie ---
    for cookie in pickle.load(open(f"cookies", "rb")):
        driver.add_cookie(cookie)
    time.sleep(1)
    driver.refresh()
    time.sleep(1)

    # # --- page scrolling ---
    # html = driver.find_element(by=By.TAG_NAME, value='html')
    # while True:
    #     size = driver.execute_script("return document.body.scrollHeight", html)
    #     html.send_keys(Keys.END)
    #     time.sleep(1.5)
    #     new_size = driver.execute_script("return document.body.scrollHeight", html)
    #     if new_size == size:
    #         break

    driver.find_element(By.XPATH, '//*[@id="__next"]/div[2]/header/div/div[3]/div/div/div[2]/button[2]').click()
    time.sleep(2)

    with open('page.html', 'w') as file:
        file.write(driver.page_source)

except Exception as e:
    print(e)
finally:
    driver.quit()
    print(f"Time: {time.time() - start_time}")


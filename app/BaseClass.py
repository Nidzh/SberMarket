import pickle
import random
import time

from fake_useragent import UserAgent
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium_stealth import stealth
from webdriver_manager.chrome import ChromeDriverManager


class BaseClass:

    def __init__(self, headless=False):
        self.useragent = UserAgent()
        self.options = webdriver.ChromeOptions()
        self.options.add_argument(f"user-agent={self.useragent.random}")
        self.options.add_experimental_option("excludeSwitches", ["enable-automation"])
        self.options.add_experimental_option('useAutomationExtension', False)

        if headless:
            self.options.add_argument("--headless")

        self.driver = webdriver.Chrome(
            options=self.options,
            service=Service(ChromeDriverManager().install())
        )
        self.driver.set_window_position(random.randint(0, 1000), random.randint(0, 1000))

        stealth(self.driver,
                languages=["ru-Ru", "ru"],
                vendor="Google Inc.",
                platform="Win32",
                webgl_vendor="Intel Inc.",
                renderer="Intel Iris OpenGL Engine",
                fix_hairline=True,
                )

    def scroll_page(self):
        html = self.driver.find_element(by=By.TAG_NAME, value='html')
        while True:
            size = self.driver.execute_script("return document.body.scrollHeight", html)
            html.send_keys(Keys.END)
            time.sleep(2)
            new_size = self.driver.execute_script("return document.body.scrollHeight", html)
            if new_size == size:
                break

    def save_html_file(self, file_name: str):
        with open(f'html/{file_name}.html', 'w') as file:
            file.write(self.driver.page_source)

    def save_cookie(self):
        pickle.dump(self.driver.get_cookies(), open("cookie", "wb"))

    def load_cookie(self):
        time.sleep(3)
        for cookie in pickle.load(open(f"cookie", "rb")):
            self.driver.add_cookie(cookie)
        time.sleep(3)
        self.driver.refresh()
        time.sleep(3)

    def find_element_by_xpath(self, value: str):
        return self.driver.find_element(By.XPATH, value)

    def find_elements_by_class_name(self, value: str):
        return self.driver.find_elements(By.CLASS_NAME, value)

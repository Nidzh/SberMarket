import json
import time
from pathlib import Path

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

        stealth(self.driver,
                languages=["ru-Ru", "ru"],
                vendor="Google Inc.",
                platform="Win32",
                webgl_vendor="Intel Inc.",
                renderer="Intel Iris OpenGL Engine",
                fix_hairline=True,
                )

    # ____________ Navigation ____________

    def find_element_by_xpath(self, value: str):
        return self.driver.find_element(By.XPATH, value)

    def find_elements_by_class_name(self, value: str):
        return self.driver.find_elements(By.XPATH, f"//*[@class='{value}']")

    def find_element_by_class_name(self, value: str):
        return self.driver.find_element(By.XPATH, f"//*[@class='{value}']")

    def scroll_page(self):
        html = self.driver.find_element(by=By.TAG_NAME, value='html')
        while True:
            size = self.driver.execute_script("return document.body.scrollHeight", html)
            html.send_keys(Keys.END)
            time.sleep(2)
            new_size = self.driver.execute_script("return document.body.scrollHeight", html)
            if new_size == size:
                break

    # ____________ Save & Load data ____________

    def save_html_file(self, file_name: str):
        filepath = Path.cwd() / 'html' / f'{file_name}.html'
        with filepath.open('w') as f:
            f.write(self.driver.page_source)

    def save_cookie(self, sleep_time: int = 5):
        time.sleep(sleep_time)
        file = self.driver.get_cookies()

        filepath = Path.cwd() / 'cookie' / 'cookie.json'
        filepath.parent.mkdir(parents=True, exist_ok=True)
        with filepath.open('w', encoding='UTF-8') as f:
            json.dump(file, f)

    def load_cookie(self):
        filepath = Path.cwd() / 'cookie' / 'cookie.json'
        with filepath.open('r', encoding='UTF-8') as f:
            cookie_list = json.load(f)
            for cookie in cookie_list:
                self.driver.add_cookie(cookie)
        time.sleep(2)
        self.driver.refresh()

    def save_local_storage_dump(self, sleep_time: int = 5):
        time.sleep(sleep_time)
        file = self.driver.execute_script(
            "var ls = window.localStorage, items = {}; "
            "for (var i = 0, k; i < ls.length; ++i) "
            "  items[k = ls.key(i)] = ls.getItem(k); "
            "return items; ")

        filepath = Path.cwd() / 'localstorage' / 'localstorage.json'
        filepath.parent.mkdir(parents=True, exist_ok=True)
        with filepath.open('w', encoding='UTF-8') as f:
            json.dump(file, f)

    def load_local_storage_dump(self):
        filepath = Path.cwd() / 'localstorage' / 'localstorage.json'
        with filepath.open('r', encoding='UTF-8') as f:
            dict = json.load(f)
            for key, value in dict.items():
                self.driver.execute_script("window.localStorage.setItem(arguments[0], arguments[1]);", key, value)
        time.sleep(2)
        self.driver.refresh()

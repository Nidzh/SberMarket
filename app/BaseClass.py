import pickle
import time

from selenium.webdriver.common.by import By
from fake_useragent import UserAgent
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
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

    def page_scrolling(self):
        from selenium.webdriver.common.keys import Keys
        html = self.driver.find_element(by=By.TAG_NAME, value='html')
        while True:
            size = self.driver.execute_script("return document.body.scrollHeight", html)
            html.send_keys(Keys.END)
            time.sleep(1.5)
            new_size = self.driver.execute_script("return document.body.scrollHeight", html)
            if new_size == size:
                break

    def save_html_file(self):
        with open('page.html', 'w') as file:
            file.write(self.driver.page_source)

    def load_cookie(self):
        for cookie in pickle.load(open(f"cookies", "rb")):
            self.driver.add_cookie(cookie)
        time.sleep(1)
        self.driver.refresh()
        time.sleep(1)

    def find_element_by_xpath(self, value: str):
        return self.driver.find_element(By.XPATH, value)

    def find_elements_by_class_name(self, value: str):
        return self.driver.find_elements(By.CLASS_NAME, value)

import time

from loguru import logger
from selenium.webdriver.common.by import By

from BaseClass import BaseClass


class SberMarketClass(BaseClass):

    def __init__(self, shop_name: str, url: str, headless=False):
        BaseClass.__init__(self, headless)
        self.url = url
        self.shop_name = shop_name
        logger.info(f'Окно {shop_name} инициализировано.')

    def get_category_list(self):
        start_time = time.time()
        logger.info('Получаем список категорий...')

        try:
            self.driver.get(self.url)
            self.load_cookie()
            self.find_element_by_xpath('//*[@id="__next"]/div[2]/header/div/div[3]/div/div/div[2]/button[2]').click()
            time.sleep(3)

            list_of_category_urls = []
            category_list = self.driver.find_elements(By.CLASS_NAME, 'CategoriesMenuListLink_styles_root__Pkyi_')
            for el in category_list:
                category_url = el.get_attribute('href')
                print(category_url)
                list_of_category_urls.append(category_url)

            return list_of_category_urls
        except Exception as e:
            print(e)
        finally:
            self.driver.quit()
            logger.info(f'Время выполнения программы {self.shop_name}: {time.time() - start_time}')

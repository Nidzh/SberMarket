import time
from loguru import logger
from app.app.BaseClass import BaseClass
from selenium.webdriver.common.by import By


class SberMarketClass(BaseClass):

    def __init__(self, shop_name: str, url: str, headless=False, browser='Chrome'):
        BaseClass.__init__(self, headless, browser)
        self.url = url
        self.shop_name = shop_name
        logger.info(f'{shop_name} запущено.')

    def get_category_list(self) -> list:
        start_time = time.time()
        logger.info('Получаем список категорий...')

        try:
            self.find_element_by_xpath('//*[@id="__next"]/div[2]/header/div/div[3]/div/div/div[2]/button[1]/div').click()
            time.sleep(5)

            # category_list = self.find_elements_by_class_name(
            #     'Link_root__iJUtm CategoriesMenuListLink_styles_root__Pkyi_ CategoriesMenuListLink_styles_rootAdaptive'
            #     '__6w5XS CategoriesMenuDrawer_styles_link__kBJbS CategoriesMenuDrawer_styles_empty__63fWG')

            category_page = self.find_element_by_class_name(
                'CategoriesMenuList_styles_root__E0jl9 CategoriesMenuDrawer_styles_list__UZtRZ')
            print(category_page.get_attribute('innerHTML'))

            # list_of_category_urls = []
            # for el in category_list:
            #     category_url = el.get_attribute('href')
            #     list_of_category_urls.append(category_url)
            #
            # return list_of_category_urls
        except Exception as e:
            print(e)
        finally:
            logger.info(f'Список категорий {self.shop_name} получен. Время выполнения: '
                        f'{time.time() - start_time}')
            self.driver.quit()

    def get_subcategory_list(self, url) -> list:
        start_time = time.time()
        logger.info('Получаем список подкатегорий...')

        try:
            self.driver.get(url)
            subcategory_list = self.find_elements_by_class_name(
                'Link_root__iJUtm LinkButton_root__ptDnR LinkButton_outline__0MjLZ LinkButton_secondary__iqQIw '
                'LinkButton_mdSize__utp6s SimpleTaxonsNav_styles_link__tigLW'
            )

            list_of_subcategory_urls = []
            for el in subcategory_list:
                subcategory_url = el.get_attribute('href')
                list_of_subcategory_urls.append(subcategory_url)

            return list_of_subcategory_urls
        except Exception as e:
            print(e)
        finally:
            logger.info(f'Список подкатегорий {self.shop_name} получен. Время выполнения: '
                        f'{time.time() - start_time}')

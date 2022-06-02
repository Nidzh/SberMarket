import time

from loguru import logger

from BaseClass import BaseClass


class SberMarketClass(BaseClass):

    def __init__(self, shop_name: str, url: str, headless=False):
        BaseClass.__init__(self, headless)
        self.url = url
        self.shop_name = shop_name
        logger.info(f'Окно {shop_name} инициализировано.')

    def get_category_list(self) -> list:
        start_time = time.time()
        logger.info('Получаем список категорий...')

        try:
            self.driver.get(self.url)
            self.load_cookie()
            self.find_element_by_xpath('//*[@id="__next"]/div[2]/header/div/div[3]/div/div/div[2]/button[2]').click()
            time.sleep(3)

            category_list = self.find_elements_by_class_name(
                'Link_root__iJUtm CategoriesMenuListLink_styles_root__Pkyi_ CategoriesMenuListLink_styles_rootAdaptive'
                '__6w5XS CategoriesMenuDrawer_styles_link__kBJbS CategoriesMenuDrawer_styles_empty__63fWG')

            list_of_category_urls = []
            for el in category_list:
                category_url = el.get_attribute('href')
                list_of_category_urls.append(category_url)

            return list_of_category_urls
        except Exception as e:
            print(e)
        finally:
            # self.driver.close()
            logger.info(f'Время выполнения программы {self.shop_name}: {time.time() - start_time}')

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

        except Exception as e:
            print(e)
        finally:
            # self.driver.close()
            logger.info(f'Время выполнения программы {self.shop_name}: {time.time() - start_time}')

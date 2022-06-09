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
            time.sleep(3)
            button = self.find_element_by_class_name(
                'Button_root__WvN9y Button_default__Ge25i Button_primary__voeOs '
                'Button_mdSize__wvr_o Button_shadow__Mtz8E styles_desktopBtn__BkiGN')

            time.sleep(1)
            button.click()

            category_page = self.find_elements_by_class_name(
                'Link_root__iJUtm CategoriesMenuListLink_styles_root__Pkyi_ CategoriesMenuListLink_styles_rootAdaptive__6w5XS CategoriesMenuDrawer_styles_link__kBJbS CategoriesMenuDrawer_styles_empty__63fWG')

            category_list = []
            for category in category_page:
                category_list.append(category.get_attribute('href'))
            return category_list

        except Exception as e:
            print(e)
        finally:
            logger.info(f'Список категорий {self.shop_name} получен. Время выполнения: '
                        f'{time.time() - start_time}')
            self.driver.quit()


    def check_validation_field(self):
        time.sleep(3)
        try:
            self.find_element_by_class_name('Checkbox_root__IGwSD').click()
            time.sleep(1)
            self.find_element_by_class_name('Button_root__WvN9y Button_default__Ge25i Button_primary__voeOs '
                                            'Button_lgSize__zpagI Button_block__kge0L Button_shadow__Mtz8E').click()
        except Exception as e:
            print(e)
        time.sleep(3)

    def remove_unnecessary_urls(self, category_list: list):
        for url in category_list:
            if 'priedlozhieniia' in url:
                category_list.remove(url)
        return category_list

    def check_cookie_field(self):
        time.sleep(2)
        try:
            self.find_element_by_class_name('Button_root__WvN9y Button_default__Ge25i '
                                            'Button_secondary__VeXhZ Button_mdSize__wvr_o').click()
            time.sleep(2)
        except Exception as e:
            print(e)


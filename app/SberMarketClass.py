from BaseClass import BaseClass
import time
from db.crud import create
from db.models import Category


class SberMarketClass(BaseClass):

    def __init__(self, url: str):
        super(SberMarketClass, self).__init__()
        self.url = url

    def get_category_list(self):

        driver = self.driver
        try:
            driver.get(self.url)
            self.load_cookie()
            self.find_element_by_xpath('//*[@id="__next"]/div[2]/header/div/div[3]/div/div/div[2]/button[2]').click()
            time.sleep(2)

            list = self.find_elements_by_class_name('CategoriesMenuListTitle_styles_root__IKPWK')
            for l in list:
                print(l)

        except Exception as e:
            print(e)
        finally:
            driver.quit()



from multiprocessing import Pool
from SberMarketClass import SberMarketClass
from BaseClass import BaseClass

GROCERYS = {
    'ЛЕНТА': 'https://sbermarket.ru/lenta?sid=262',
    'МАГНИТ': 'https://sbermarket.ru/magnit_express?sid=4690',
    'ГЛОБУС': 'https://sbermarket.ru/globus?sid=1947',
    'ВКУСВИЛЛ': 'https://sbermarket.ru/vkusvill?sid=3960',
    'ВЕРНЫЙ': 'https://sbermarket.ru/verniy_fd?sid=5972',
    'METRO': 'https://sbermarket.ru/metro?sid=86',
    'АШАН': 'https://sbermarket.ru/auchan?sid=333',
    'АШАН СУПЕРМАРКЕТ': 'https://sbermarket.ru/auchansm?sid=12965'
}

if __name__ == '__main__':
    for key, value in GROCERYS.items():
        window = SberMarketClass(value)
        window.get_category_list()
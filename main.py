import time
from app.app.SberMarketClass import SberMarketClass
from loguru import logger
from pathlib import Path
shop_list = (
    ('ЛЕНТА', 'https://sbermarket.ru/lenta?sid=262'),
    ('МАГНИТ', 'https://sbermarket.ru/magnit_express?sid=4690'),
    ('ГЛОБУС', 'https://sbermarket.ru/globus?sid=1947'),
    ('ВКУСВИЛЛ', 'https://sbermarket.ru/vkusvill?sid=3960'),
    ('ВЕРНЫЙ', 'https://sbermarket.ru/verniy_fd?sid=5972'),
    ('METRO', 'https://sbermarket.ru/metro?sid=86'),
    ('АШАН', 'https://sbermarket.ru/auchan?sid=333'),
    ('АШАН СУПЕРМАРКЕТ', 'https://sbermarket.ru/auchansm?sid=12965')
)

if __name__ == '__main__':

    for shop in shop_list:
        logger.add(Path.cwd()/'logs'/'logs.log', level='DEBUG')
        logger.info('Запуск парсера...')

        window = SberMarketClass(shop_name=shop[0], url=shop[1], headless=False)
        window.driver.get(window.url)
        window.save_local_storage_dump()




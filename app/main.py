import multiprocessing
import time
from loguru import logger

from SberMarketClass import SberMarketClass

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
    logger.add('logs/logs.log', level='DEBUG')
    logger.info('Запуск парсера...')
    start_time = time.time()


    def pool_thread(shop):
        window = SberMarketClass(shop_name=shop[0], url=shop[1], headless=False)
        window.get_category_list()


    with multiprocessing.Pool(multiprocessing.cpu_count() // 2) as pool:
        pool.map(pool_thread, shop_list)

    logger.info(f'Общее время выполнения программы : {time.time() - start_time}')

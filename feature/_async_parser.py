import datetime
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import aiohttp
import aiofiles
import asyncio

shop_list = {
    'METRO': 'https://sbermarket.ru/metro?sid=86',
    'АШАН': 'https://sbermarket.ru/auchan?sid=333',
    'АШАН СУПЕРМАРКЕТ': 'https://sbermarket.ru/auchansm?sid=12965',
    'ЛЕНТА': 'https://sbermarket.ru/lenta?sid=262',
    'МАГНИТ': 'https://sbermarket.ru/magnit_express?sid=4690',
    'ГЛОБУС': 'https://sbermarket.ru/globus?sid=1947',
    'ВКУСВИЛЛ': 'https://sbermarket.ru/vkusvill?sid=3960',
    'ВЕРНЫЙ': 'https://sbermarket.ru/verniy_fd?sid=5972'
}

async def get_all_categorys():
    ua = UserAgent()

    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'User-Agent': ua.random
    }

    async with aiohttp.ClientSession() as session:
        for shop_name, url in shop_list.items():
            response = await session.get(url=url, headers=headers)
            text = await response.text()
            # soup = BeautifulSoup(await response.text(), 'lxml')
            async with aiofiles.open(f'{shop_name}.html', mode='w') as f:
                await f.write(text)

async def main():
    await get_all_categorys()


if __name__ == '__main__':
    asyncio.run(main())

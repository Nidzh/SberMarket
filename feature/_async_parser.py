import asyncio
import aiofiles
import aiohttp
from bs4 import BeautifulSoup
from fake_useragent import UserAgent


async def get_all_categories(shop_list):
    ua = UserAgent()

    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'User-Agent': ua.random
    }

    async with aiohttp.ClientSession() as session:
        for shop_name, url in shop_list.items():
            response = await session.get(url=url, headers=headers)
            text = await response.text()
            soup = BeautifulSoup(await response.text(), 'lxml')
            async with aiofiles.open(f'{shop_name}.html', mode='w') as f:
                await f.write(text)


async def main():
    await get_all_categories()


if __name__ == '__main__':
    asyncio.run(main())

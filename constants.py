SHOP_LIST = {
    # 'METRO': 'https://sbermarket.ru/metro?sid=86',
    'АШАН': 'https://sbermarket.ru/auchan?sid=333',
    'АШАН СУПЕРМАРКЕТ': 'https://sbermarket.ru/auchansm?sid=12965',
    'ЛЕНТА': 'https://sbermarket.ru/lenta?sid=262',
    'МАГНИТ': 'https://sbermarket.ru/magnit_express?sid=4690',
    'ГЛОБУС': 'https://sbermarket.ru/globus?sid=1947',
    'ВКУСВИЛЛ': 'https://sbermarket.ru/vkusvill?sid=3960',
    'ВЕРНЫЙ': 'https://sbermarket.ru/verniy_fd?sid=5972'
}

key_list = list(SHOP_LIST.keys())
val_list = list(SHOP_LIST.values())
position = val_list.index('https://sbermarket.ru/auchan?sid=333')
print(key_list[position])
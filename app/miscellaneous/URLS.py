categories = ['https://sbermarket.ru/metro/c/priedlozhieniia/skidki?sid=86',
              'https://sbermarket.ru/metro/c/priedlozhieniia/shchiedryie-vykhodnyie?sid=86',
              'https://sbermarket.ru/metro/c/priedlozhieniia/kibierdni?sid=86',
              'https://sbermarket.ru/metro/c/na-dachu-s-bonusami-sber?sid=86',
              'https://sbermarket.ru/metro/c/alcohol-new?sid=86',
              'https://sbermarket.ru/metro/c/ovoshchi-frukty-oriekhi?sid=86',
              'https://sbermarket.ru/metro/c/moloko-iaitsa-new?sid=86',
              'https://sbermarket.ru/metro/c/miaso-ptitsa-new?sid=86',
              'https://sbermarket.ru/metro/c/ryba-morieprodukty-new-new?sid=86',
              'https://sbermarket.ru/metro/c/gotovaia-ieda?sid=86',
              'https://sbermarket.ru/metro/c/zamorozhiennyie-produkty?sid=86',
              'https://sbermarket.ru/metro/c/bakalieia-new?sid=86',
              'https://sbermarket.ru/metro/c/zdorovoie-pitaniie?sid=86',
              'https://sbermarket.ru/metro/c/piknik-i-otdikh-na-dache?sid=86',
              'https://sbermarket.ru/metro/c/voda-soki-napitki-new?sid=86',
              'https://sbermarket.ru/metro/c/kolbasy-sosiski-dielikatiesy-new?sid=86',
              'https://sbermarket.ru/metro/c/syry?sid=86',
              'https://sbermarket.ru/metro/c/chaj-kofe_new_osnovnaya?sid=86',
              'https://sbermarket.ru/metro/c/sladosti-new?sid=86',
              'https://sbermarket.ru/metro/c/khlieb-vypiechka-new?sid=86',
              'https://sbermarket.ru/metro/c/konsiervy-solienia-new?sid=86',
              'https://sbermarket.ru/metro/c/sousy-spietsii-maslo?sid=86',
              'https://sbermarket.ru/metro/c/chipsy-snieki-new?sid=86',
              'https://sbermarket.ru/metro/c/recepty-producty?sid=86',
              'https://sbermarket.ru/metro/c/sobstvennie-marki-metro?sid=86',
              'https://sbermarket.ru/metro/c/unikalnie-predlozhieniia-metro?sid=86',
              'https://sbermarket.ru/metro/c/bytovaia-khimiia-uborka-new?sid=86',
              'https://sbermarket.ru/metro/c/dietskiie-tovary?sid=86',
              'https://sbermarket.ru/metro/c/kosmietika-ghighiiena-new?sid=86',
              'https://sbermarket.ru/metro/c/tovary-dlia-zhivotnykh?sid=86',
              'https://sbermarket.ru/metro/c/mielochi-vozlie-kassy?sid=86',
              'https://sbermarket.ru/metro/c/dlia-doma-i-dachi?sid=86',
              'https://sbermarket.ru/metro/c/dacha-i-sad?sid=86',
              'https://sbermarket.ru/metro/c/bitovaya-tekhnika-elektronika?sid=86',
              'https://sbermarket.ru/metro/c/odiezhda-obuv-aksiessuary?sid=86',
              'https://sbermarket.ru/metro/c/kantsieliariia?sid=86', 'https://sbermarket.ru/metro/c/avtotovary?sid=86',
              'https://sbermarket.ru/metro/c/sportivnyie-tovary?sid=86',
              'https://sbermarket.ru/metro/c/vsie-dlia-riemonta?sid=86']


def remove_unnecessary_urls(category_list: list):
    for url in category_list:
        if 'priedlozhieniia' in url:
            category_list.remove(url)
    return category_list


print(remove_unnecessary_urls(categories))

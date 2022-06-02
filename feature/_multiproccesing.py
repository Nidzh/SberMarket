# def pool_thread(shop):
#     window = SberMarketClass(shop_name=shop[0], url=shop[1], headless=False)
#     window.get_category_list()
#
#
# with multiprocessing.Pool(4) as pool:
#     pool.map(pool_thread, shop_list)
# --- set proxy ---
# options.add_argument("--proxy-server=138.128.91.65:8000")


# # --- page scrolling ---
# from selenium.webdriver.common.keys import Keys
# html = driver.find_element(by=By.TAG_NAME, value='html')
# while True:
#     size = driver.execute_script("return document.body.scrollHeight", html)
#     html.send_keys(Keys.END)
#     time.sleep(1.5)
#     new_size = driver.execute_script("return document.body.scrollHeight", html)
#     if new_size == size:
#         break


# # --- save html file ---
# with open('page.html', 'w') as file:
#     file.write(driver.page_source)
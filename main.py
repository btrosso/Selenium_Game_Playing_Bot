import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

COOKIE_URL = "http://orteil.dashnet.org/experiments/cookie/"

chrome_driver_path = "C:\Development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get(COOKIE_URL)

cookie = driver.find_element_by_css_selector("#cookie")






# # get all the upgrade elements
# upgrades = driver.find_elements_by_css_selector("#rightPanel #store div")
# # delete the last one in the list (its empty)
# del upgrades[-1]
# # convert to text for readability
# upgrades_text = [upgrade.text for upgrade in upgrades]
# # create list of prices
# upgrade_prices = [int(upgrade.split("- ")[1].split("\n")[0].replace(",", "")) for upgrade in upgrades_text]
# # create a dictionary to work with all the pieces
# upgrades_dict = {}
# for num in range(len(upgrades)):
#     upgrades_dict[num] = {
#         "name": upgrades_text[num],
#         "price": upgrade_prices[num],
#         "element": upgrades[num]
#     }
# print(upgrades_dict)
#
# def check_for_upgrades(upgrades: dict) -> int:
#     current_cookies = int(driver.find_element_by_css_selector("#money").text)
#     index = len(upgrades)-1
#     for _ in range(len(upgrades)):
#         if upgrades[index]["price"] < current_cookies:
#             return index
#         else:
#             index -= 1
#
# # 5 minutes from now
# # timeout = time.time() + 60*5
# # test timeout - the number at the end is in seconds
# timeout = time.time() + 30
#
# while time.time() < timeout:
#     cookie.click()
#     if int(time.time()) % 5 == 0:
#         try:
#             element = upgrades[check_for_upgrades(upgrades_dict)]
#             element.click()
#         except TypeError:
#             pass


import time
from selenium import webdriver

COOKIE_URL = "http://orteil.dashnet.org/experiments/cookie/"
chrome_driver_path = "C:\Development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get(COOKIE_URL)
cookie = driver.find_element_by_css_selector("#cookie")

# grab the items from the store menu
items = driver.find_elements_by_css_selector("#store div")
# grab their ids
item_ids = [item.get_attribute("id") for item in items]

timeout = time.time() + 5
five_min = time.time() + 60*5  # 5minutes

while True:
    cookie.click()

    # Every 5 seconds:
    if time.time() > timeout:
        # get price elements to work with
        all_prices = driver.find_elements_by_css_selector("#store b")
        prices = []

        # turn the prices into valid integers and add to prices list
        for price in all_prices:
            price_text = price.text
            if price_text != "":
                cost = int(price_text.split("-")[1].strip().replace(",", ""))
                prices.append(cost)

        # create a dictionary with the prices and ids
        cookie_upgrades = {}
        for n in range(len(prices)):
            cookie_upgrades[prices[n]] = item_ids[n]

        # grab the money element to work with and turn into a valid int
        money_element = driver.find_element_by_id("money").text
        if "," in money_element:
            money_element = money_element.replace(",", "")
        cookie_count = int(money_element)

        # find the upgrades currently affordable
        affordable_upgrades = {}
        for cost, id in cookie_upgrades.items():
            if cookie_count > cost:
                affordable_upgrades[cost] = id

        # find the most expensive upgrade we can currently afford
        most_expensive_upgrade = max(affordable_upgrades)
        print(most_expensive_upgrade)
        buy_this_upgrade_id = affordable_upgrades[most_expensive_upgrade]

        driver.find_element_by_id(buy_this_upgrade_id).click()

        # add another 5 seconds until the next click
        timeout = time.time() + 5

        #After 5 minutes stop the bot and check the cookies per second count.
        if time.time() > five_min:
            cookie_per_s = driver.find_element_by_id("cps").text
            print(cookie_per_s)
            break

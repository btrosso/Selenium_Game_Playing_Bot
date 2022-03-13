from selenium import webdriver

chrome_driver_path = "C:\Development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://www.amazon.com")

# closes a single active tab
driver.close()
# quit will kill the entire browser (in case there are multiple windows open)
driver.quit()
from selenium import webdriver

chrome_driver_path = "/Users/david/Documents/Development/chromedriver"
driver = webdriver.Chrome(executable_path = chrome_driver_path)
driver.get("https://www.amazon.es")
driver.close()
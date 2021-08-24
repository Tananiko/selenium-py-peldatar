from selenium import webdriver
PATH = "/Users/tarjanyibela/Downloads/chromedriver"

driver = webdriver.Chrome(PATH)
driver.get("https://www.hirkereso.hu")
driver.close()

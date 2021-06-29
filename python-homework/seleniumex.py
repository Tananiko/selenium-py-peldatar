
# Készíts egy Python alkalmazást ami selenium - ot használ.Nyisson meg egy Chrome böngészöt és töltsön be
# egy tetszőleges weblapot az Internetről.Az oldalon probáld megtalálni a < div id = "nemletezik" > < / div > mezőt.\
# A lényeg, hogy hibát dogjon a driver.find_by_id függvényhívás.Feladatot, hogy kezeld le ezt a hibát és írj ki
# valami emberileg olvasható üzenetet.Extra feladatként készíts egy saját függvényt, ami bármilyen find_by_id
# lokátor hívásnál lekezeli a nemlétező elem tipusú hibát.A megoldáshoz használj python try except struktúrát.
# A megoldást egy seleniumex.py nevű fileban kell beadnod.

from selenium import webdriver
PATH = "/Users/tarjanyibela/Downloads/chromedriver"
from selenium.common.exceptions import NoSuchElementException
driver = webdriver.Chrome(PATH)
driver.get("https://refx.com/signup/")
try:

    webElement = driver.find_element_by_id("privacy-policy")
    webElement.click()
except NoSuchElementException as exception:
    print("Element not found and test failed")



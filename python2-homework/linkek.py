# Készíts egy Python alkalmazást ami selenium-ot használ. Indítsd el lokálisan a
# selenium-py-peldatar alkalmazást. A program töltse be a példatárból az http://localhost:9999 oldalt.
# Lokátorral keresd ki az összes linket az oldalról. Tárold a memóriában egy listában az összes linket.
# A list tartalmát írd ki egy fájlba. Minden link egy új sorba kerüljön. A kimenetre írd ki hány linket találtál
# A megoldást egy linkek.py nevű file-ban kell beadnod.

from selenium import webdriver
PATH = "/Users/tarjanyibela/Downloads/chromedriver"
URL = "https://gentle-bay-0e4e13803.azurestaticapps.net"

browser = webdriver.Chrome(PATH)
browser.maximize_window()
browser.get(URL)

link_list = browser.find_elements_by_xpath('//a')
href_link = []
for i in link_list:
    href_link.append(i.get_attribute("href"))
    browser.quit

my_txt = open(data.txt, 'w')
for i in href_link:
    my_text.write(i)
    my_txt.write("\n")
print(len(href_link))


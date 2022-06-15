# import webdriver
import time

from selenium import webdriver
#
driver = webdriver.Chrome()
#
driver.maximize_window()
# obtenir l'url de la page
driver.get("https://demo.nopcommerce.com/")
# création de la variable url_page
url_page = driver.current_url
print(url_page)
# obtenir le titre de la page
titrePage = driver.title
print(titrePage)
# obtenir le code source de la page
page_source = driver.page_source
print(page_source)

time.sleep(3)
driver.quit()
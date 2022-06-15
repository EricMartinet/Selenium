# import webdriver
import time

from selenium import webdriver
driver = webdriver.Chrome()
# obtenir l'url de la page
driver.get("https://demo.nopcommerce.com/")
# arret
time.sleep(3)
# aller sur google
driver.get("https://www.google.com")
time.sleep(3)
# navigation
driver.back()
time.sleep(3)
driver.forward()
# actualisation
driver.refresh()
# Avant le driver close ça fermait pas toutes les fenetres
# driver.close()
driver.quit()
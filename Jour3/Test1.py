# Test case
# 1 lancer le navigateur
# 2 accéder à https://demo.nopcommerce.com/
# 3 cliquer sur le lien enregister
# 4 remplir le forumulaire
# 5 cliquer sur le bouton register

import time
# Importer le pilote
from selenium import webdriver
# 1 Création d'une instance de chrome
from selenium.webdriver.common.by import By

driver =webdriver.Chrome()
# l'affichage étant partiel on ouvre la fenetre en grand
driver.maximize_window()
# 2 accéder au
driver.get("https://demo.nopcommerce.com/")
# par link text
driver.find_element(By.LINK_TEXT, "Register").click()
# driver.find_element(By.lINK_TEXT, "Register").click()
# ou partiel : driver.find_element(By.PARTIAL_LINK_TEXT, "Regist").click()
# driver.find_element(By.ID, "Register").click()
driver.find_element(By.ID, "FirstName").send_keys("ERic Rick")
driver.find_element(By.ID, "LastName").send_keys("Riri")
driver.find_element(By.ID, "Email").send_keys("yo@gmail.com")
driver.find_element(By.ID, "Password").send_keys("123456")
driver.find_element(By.ID, "ConfirmPassword").send_keys("123456")
# driver.find_element(By.ID, "register-button").click()
driver.find_element(By.ID, "register-button").submit()
# driver.close()
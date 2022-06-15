# Test Case
# ------------------
# 1) Ouvrir le navigateur(chrome/firefox/Edge)
# 2) Naviguer vers l'url https://www.saucedemo.com/
# 3) Entrer username (standard_user)
# 4) Entrer password (secre_sauce)
# 5) Cliquer sur le bouton Login
# 6) Aller dans le panier en cliquant sur l'image shopping_cart_link
# 7) Revenir à la page de magasinage en cliquant sur le bouton continue-shopping
# 8) ajouter un item en cliquant sur add-to-cart-sauce-labs-backpack
# 9) aller dans le panier en cliquant sur l'image shopping_cart_link
# 10) enlever l'item du panier en cliquant sur le bouton remove-sauce-labs-backpack

# importer le pilote
import time

from selenium import webdriver
# 1 création d'une instance de chrome
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
# affichage de la fenetre en grand
driver.maximize_window()
# 2 accéder au site
driver.get("https://www.saucedemo.com/")
# 3 entrer login
driver.find_element(By.ID, "user-name").send_keys("standard_user")
# 4 entrer password
driver.find_element(By.ID, "password").send_keys("secret_sauce")
# 5 cliquer sur submit
driver.find_element(By.ID, "login-button").submit()

# 6 aller sur le panier d'achats: cliquer sur le cart
driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
# 7 cliquer sur le bouton continue shopping
driver.find_element(By.ID,"continue-shopping").click()

#  8 ajouter un item
driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
#  9 aller dans le kart :
driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
#  10 enlever l'item du panier
driver.find_element(By.ID, "remove-sauce-labs-backpack").click()

# Attendre 3 secondes
time.sleep(3)

# fermeture du pilote
driver.close()

# Test Cases
# 1- Importer webdriver
# 2- Créer une instance de Chrome et agrandir la fenêtre
# 3- Ouvrir la page http://demo.automationtesting.in/Frames.html
# 4- Fenêtre principale : Cliquer sur 'Single Iframe'
# 5- Passer à la iframe
# 6- iframe1 : écrire le texte dans la zone de saisie : 'tralala'
# 7- Retour à la fenetre principale
# 8- Fenêtre principale : Cliquer sur 'Iframe with in an Iframe'
# 9- Passer à la iframe Multiple sans ID et sans class name via une variable et XPATH '//*[@id="Multiple"]/iframe'
# 10- Passer à la iframe imbriquée simple sans ID           via une variable et XPATH "//div[@class='row']/iframe"
# 11- iframe imbriquée : écrire le texte dans la zone de saisie : 'itou'
# 12- Revenir à la page principale
# 13- Fenêtre principale : Cliquer sur 'Single Iframe'
import time
# 1- Importer webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
# 2- Créer une instance de Chrome et agrandir la fenêtre
driver = webdriver.Chrome()
driver.maximize_window()
# 3- Ouvrir la page http://demo.automationtesting.in/Frames.html
driver.get('http://demo.automationtesting.in/Frames.html')
# 4- Fenêtre principale : Cliquer sur 'Single Iframe'
driver.find_element(By.LINK_TEXT, 'Single Iframe').click()
# 5- Passer à la iframe par son id ou son class name
driver.switch_to.frame('singleframe')
# 6- iframe1 : écrire le texte dans la zone de saisie : 'tralala'
driver.find_element(By.XPATH, "//div[@class='col-xs-6 col-xs-offset-5']/input").send_keys('tralalala')
time.sleep(2)
# 7- Retour à la fenetre principale
driver.switch_to.default_content()
# 8- Fenêtre principale : Cliquer sur 'Iframe with in an Iframe'
driver.find_element(By.LINK_TEXT, 'Iframe with in an Iframe').click()
time.sleep(2)
# 9- Passer à la iframe Multiple '//*[@id="Multiple"]/iframe'
iframeMultiple = driver.find_element(By.XPATH, '//*[@id="Multiple"]/iframe')
driver.switch_to.frame(iframeMultiple)
# 10- Passer à la iframe imbriquée simple "//div[@class='row']/iframe"
iframeSingle = driver.find_element(By.XPATH, "//div[@class='row']/iframe")
driver.switch_to.frame(iframeSingle)
# 11- iframe imbriquée : écrire le texte dans la zone de saisie : 'itou'
driver.find_element(By.XPATH, "//div[@class='col-xs-6 col-xs-offset-5']/input").send_keys('itou')
time.sleep(2)
# 12- Revenir à la page principale
# Retour à la frame parent : x2 !!!!!
driver.switch_to.parent_frame()
driver.switch_to.parent_frame()
# ou simplement :
# driver.switch_to.default_content()
time.sleep(2)
# 13- Fenêtre principale : Cliquer sur 'Single Iframe'
driver.find_element(By.LINK_TEXT, 'Single Iframe').click()
time.sleep(2)
# Fermer les fenêtres
driver.quit()
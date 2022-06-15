# Test Cases
# 1- Importer webdriver
# 2- Créer une instance de Chrome et agrandir la fenêtre
# 3- Ouvrir la page https://the-internet.herokuapp.com/javascript_alerts
# 4- Fenêtre principale : Cliquer sur le bouton Alert
# 5- Passer à la fenêtre d'Alerte
# 6- Alerte : Récupérer le message de la fenêtre d'Alerte
# 7- Alerte : Cliquer sur OK
# 8- Fenêtre principale : Imprimer le message affiché result
# 9- Fenêtre principale : Cliquer sur le 2ième bouton
# 10- Passer à la fenêtre de Confirmation
# 11- Confirmation : Récupérer le message de la fenêtre de Confirmation
# 12- Confirmation : Cliquer sur Annuler
# 13- Fenêtre principale : Imprimer le message affiché result
# 14- Fenêtre principale : Cliquer sur le bouton dont le texte est 'Click for JS Prompt'
# 15- Passer à la fenêtre de Prompt
# 16- Prompt : Récupérer le message de la fenêtre de prompt
# 17- Prompt : Saisir 'hoooohooooo'
# 18- Prompt : accepter
# 19- Fenêtre principale : Imprimer le message affiché result
# 20- Fermer toutes les fenêtres
import time
# 1- Importer webdriver

from selenium import webdriver
from selenium.webdriver.common.by import By
# 2- Créer une instance de Chrome et agrandir la fenêtre
driver = webdriver.Chrome()
driver.maximize_window()
# 3- Ouvrir la page https://the-internet.herokuapp.com/javascript_alerts
driver.get('https://the-internet.herokuapp.com/javascript_alerts')
# 4- Fenêtre principale : Cliquer sur le bouton Alert
driver.find_element(By.XPATH, "//button[contains(text(), 'Alert')]").click()
# 5- Passer à la fenêtre d'Alerte
alert_window = driver.switch_to.alert
# 6- Alerte : Récupérer le message de la fenêtre d'Alerte
print("le texte de l'alerte est : ", alert_window.text)
time.sleep(1)
# 7- Alerte : Cliquer sur OK
alert_window.accept()
# 8- Fenêtre principale : Imprimer le message affiché result
print(driver.find_element(By.ID, "result").text)
time.sleep(1)
# 9- Fenêtre principale : Cliquer sur le 2ième bouton
driver.find_element(By.XPATH, "(//button)[2]").click()

# 10- Passer à la fenêtre de Confirmation
confirm_window = driver.switch_to.alert
# 11- Confirmation : Récupérer le message de la fenêtre de Confirmation
print("texte de la confirmation : ", confirm_window.text)
time.sleep(1)
# 12- Confirmation : Cliquer sur Annuler
confirm_window.dismiss()
time.sleep(1)
# 13- Fenêtre principale : Imprimer le message affiché result
print(driver.find_element(By.ID, "result").text)
# 14- Fenêtre principale : Cliquer sur le bouton dont le texte est 'Click for JS Prompt'
driver.find_element(By.XPATH, "//button[text()='Click for JS Prompt']").click()
# 15- Passer à la fenêtre de Prompt
prompt_window = driver.switch_to.alert
# 16- Prompt : Récupérer le message de la fenêtre de prompt
print("message prompt : ", prompt_window.text)

# 17- Prompt : Saisir 'hoooohooooo'
prompt_window.send_keys('hoooohooooo')
time.sleep(2)
# 18- Prompt : accepter
prompt_window.accept()
# 19- Fenêtre principale : Imprimer le message affiché result
print(driver.find_element(By.ID, "result").text)
time.sleep(2)
# 20- Fermer toutes les fenêtres
driver.quit()
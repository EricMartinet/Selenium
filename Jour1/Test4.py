#Test Case
#------------------
# 1) Ouvrir le navigateur(chrome/firefox/Edge)
# 2) Naviguer vers l'url https://login.salesforce.com/
# 3) Entrer username (Admin)
# 4) Entrer password (admin123)
# 5) Cliquer sur le bouton Login
# 6) recuperer le titre de la page(titre actuel)
# 7) Verifier le titre de la page: Connexion | Salesforce  (attendu)
# 8) Vérifier le message d'erreur
# 9) Fermer le navigateur
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

#service_obj = Service("C:\\Users\\ericm\OneDrive\\Documents\\AEC\\Drivers\\chromedriver.exe")
# 1) Ouvrir le navigateur(chrome/firefox/Edge)
#driver = webdriver.Chrome(service=service_obj)
# 2) Naviguer vers l'url https://opensource-demo.orangehrmlive.com/
# En mettant le driver chromedriver.exe dans le dossier Script de la bibliothèque de python on économise de spécifier
# le chemin
driver = webdriver.Chrome()
driver.get("https://login.salesforce.com/")
driver.maximize_window()
# 3) Entrer username (Admin)
driver.find_element(By.ID, "username").send_keys("Eric")
# 4) Entrer password (admin123)
driver.find_element(By.ID, "password").send_keys("Eric")
# 5) Cliquer sur le bouton Login
driver.find_element(By.ID, "Login").click()
# 6) recuperer le titre de la page(titre actuel)
act_title = driver.title
exp_title = "Connexion | Salesforce"
# 7) Verifier le titre de la page: Connexion | Salesforce  (attendu/expected)
if act_title == exp_title:
    print("Le test de connection  est passed")
else:
    print("Le test de connection a la page  est failed")


#8) Vérifier le message d'erreur
act_msg_error = driver.find_element(By.ID, "error").text
exp_msg_error = "Vérifiez votre nom d'utilisateur et votre mot de passe. Si vous ne parvenez toujours pas à vous connecter, contactez votre administrateur Salesforce."
if exp_msg_error == act_msg_error:
    print("Le test Login message d'erreur a réussi")
else:
    print("Le test Login message d'erreur a échoué")
   # print("le message d'erreur est: " + exp_msg_error)
# Mecanisme d'attente pour debuggage : 4 secondes
time.sleep(4)
# 8) Fermer le navigateur
driver.close()
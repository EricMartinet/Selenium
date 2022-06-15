# Test Cases

# 1- importer selenium webdriver
# 2- créer une instance de chrome
# 3- aller sur google.com
# 4- saisir "selenium r" dans la recherche
# 5- cliquer sur le choix prérenseigné à "selenium robot framework"
# -------------------------------------------------------------------------------
# 1- importer selenium webdriver
from datetime import time
import time

from selenium import webdriver
# 2- créer une instance de chrome
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
pilote = webdriver.Chrome()
time.sleep(3)
# 3- aller sur google.com
pilote.get("https://www.google.com")
time.sleep(3)
# 4- saisir selenium dans la recherche
phraseRecherchee = "selenium robot framework"
pilote.find_element(By.XPATH, "//input[@class='gLFyf gsfi']").send_keys("pshhhhhhhh")
time.sleep(2)
pilote.find_element(By.XPATH, "//input[@class='gLFyf gsfi']").clear()
time.sleep(1)
# boucle for avec un indice numéral : i de 0 jusqu'à la taille du tableau
for i in range(len(phraseRecherchee)):
    pilote.find_element(By.XPATH, "//input[@class='gLFyf gsfi']").send_keys(phraseRecherchee[i])
    time.sleep(1)
    try:
        pilote.find_element(By.XPATH, "//span[. = '" + phraseRecherchee + "']")
        print("Trouvé dans la liste avec la saisie de : '" + phraseRecherchee[0:i+1]+"'")
# 5- cliquer sur le choix prérenseigné à "selenium robot framework"
        pilote.find_element(By.XPATH, "//span[. = '" + phraseRecherchee + "']").click()
        time.sleep(3)
        break
    except NoSuchElementException:
        print("Pas encore trouvé avec la saisie de : '" + phraseRecherchee[0:i+1]+"'")
# Fermeture de la page
pilote.quit()
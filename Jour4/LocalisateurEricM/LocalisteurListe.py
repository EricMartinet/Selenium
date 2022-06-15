# Test Cases

# 1- importer selenium webdriver
# 2- créer une instance de chrome
# 3- aller sur google.com
# 4- saisir "selenium " dans la recherche
# 5- le choix prérenseigné à "selenium robot framework" n'existe pas
# 6- vérifier qu'il existe bien 10 suggestions différentes
# -------------------------------------------------------------------------------
# 7 - compléter la saisie avec un "r" dans la recherche pour obtenir "selenium r"
# 5- sélectionner le choix prérenseigné à "selenium robot framework" et clicker dessus
# 6- redirection vers la page google de recherche de google correspondante
# 1- importer selenium webdriver
from datetime import time
import time

from selenium import webdriver
# 2- créer une instance de chrome
from selenium.webdriver.common.by import By
# pilote = webdriver.Chrome()
# Pour enlever le message d'avertissement "Chrome est contrôlé par un logiciel de test automatisé" en haut de la fenêtre
chrome_options = webdriver.ChromeOptions();
chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])
pilote = webdriver.Chrome(options=chrome_options)
time.sleep(3)
# 3- aller sur google.com
pilote.get("https://www.google.com")
time.sleep(3)
# 4- saisir selenium dans la recherche
pilote.find_element(By.XPATH, "//input[@class='gLFyf gsfi']").send_keys("selenium ")
time.sleep(3)
# prendre un instantanné :
pilote.save_screenshot("listeSuggestions.png")
# 5- sélectionner le choix prérenseigné à selenium robotframework
# Récupérer la liste des choix suggérés
# !!!!!! Attention utiliser la méthode find_elementssssssssssss avec un S !!!!!!!!
# FONCTIONNE AVEC :
# Xpath absolu
# list_suggestions = pilote.find_elements(By.XPATH, "/html[1]/body[1]/div[1]/div[3]/form[1]/div[1]/div[1]/div[2]/div[2]/div[2]/ul[1]/div[1]/ul[1]/li")
# Xpath relatifs
list_suggestions = pilote.find_elements(By.XPATH, "//ul[@role='listbox']//ul[@role='listbox']/li")
# list_suggestions = pilote.find_elements(By.XPATH, "//div[@class='wM6W7d']/span")
# NE FONCTIONNE PAS AVEC :
# list_suggestions = pilote.find_elements(By.XPATH, "//li[@class='sbct']")
# il manque l'élément qui est pointé par la souris

# suggestion = pilote.find_elements(By.XPATH, "//ul[@role='listbox']//ul[@role='listbox']/li[contains(text, 'webdriver')]")



print("Le nombre d\'éléments récupérés est : ", len(list_suggestions))
recherche = "selenium webdriver"
trouve = False
compteur = 0
indice = 0
for suggestion in list_suggestions:
    if not (suggestion.text == ""):
        compteur += 1
        print(str(compteur)+". ", suggestion.text)
    if recherche in suggestion.text :
        print("*** trouvé !!***")
        trouve = True
        indice = compteur
#        break
# 6- Vérification du nombre de suggestions = 10?
print("Le nombre de suggestions est :", compteur)
if not trouve:
    print(recherche,"n'est pas dans la liste")
else :
    list_suggestions[indice-1].click()

time.sleep(3)

# Fermeture de la page
pilote.quit()




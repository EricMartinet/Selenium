#  Test Cases
# 1- importer selenium webdriver
# 2- créer une instance de chrome et agrandir la fenêtre
# 3- aller sur https://omayo.blogspot.com
# 4 - Récupérer les options du multichoix multiselect1
# 5- cliquer sur Swift
# Pour que l'éditeur puisser reconnaître les items comme WebElements : utiliser find_elements
# 6- cliquer sur l'option selectionnée
# 7- cliquer sur l'option Volvo
# 8- selectionner Audi par value audix
# 9- selectionner le premier item
# 10- déselectionner tout
# 11- Récupérer les choix du dropdown 1 :
# 12- imprimer dans la console la premiere option selectionnee
# 13- selectionner le deuxieme choix
# 14- selectionner l'option par valeur = def#

import time
from optparse import Option

# 1- importer selenium webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

# 2- créer une instance de chrome et agrandir la fenêtre
driver = webdriver.Chrome()
driver.maximize_window()
# 3- aller sur https://omayo.blogspot.com
driver.get('https://omayo.blogspot.com')
time.sleep(1)
# 4- Récupérer les options du multichoix multiselect1
multiSelectBrand = Select(driver.find_element(By.ID, 'multiselect1'))
for opt in multiSelectBrand.options:
# 5- cliquer sur Swift
    if opt.text == 'Swift':
        opt.click()
        time.sleep(1)
# Pour que l'éditeur puisser reconnaître les items comme WebElements :
tableauOptions = driver.find_elements(By.XPATH, "//select[@id='multiselect1']/option")
for option in tableauOptions:
# 6- cliquer sur l'option selectionnée
    if option.is_selected():
        option.click()
        time.sleep(1)
# 7- cliquer sur l'option Volvo
if option.text == 'Volvo':
        option.click()
        time.sleep(1)

# méthodes de la classe Select :
# 8- selectionner Audi par value audix
multiSelectBrand.select_by_value('audix')
time.sleep(1)
# 9- selectionner le premier item
multiSelectBrand.select_by_index(1)
time.sleep(1)
# 10- déselectionner tout
multiSelectBrand.deselect_all()
time.sleep(1)

# 11- Récupérer les choix du dropdown 1 :
drop1 = Select(driver.find_element(By.XPATH, "//select[@id='drop1']"))
# 12- imprimer dans la console la premiere option selectionnee
print(drop1.first_selected_option.text)
# 13- selectionner le deuxieme choix
drop1.select_by_index(2)
time.sleep(1)
# 14- selectionner l'option par valeur = def
drop1.select_by_value('def')
time.sleep(1)

driver.quit()

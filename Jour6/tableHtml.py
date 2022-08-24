import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/")

# Calculer un script qui calcule le nombre de lignes du tableau
raws = driver.find_elements(By.XPATH, "//table[@name='BookTable']/tbody/tr")
print('la table possède :', len(raws), ' lignes')
# Compter le nombre de colonnes du tableau
cols = driver.find_elements(By.XPATH, "//table[@name='BookTable']/tbody/tr/th")
# ou                                    //table[@name='BookTable']//th
print('le tableau possède :', len(cols), 'colonnes')
# récupérer le texte de la troisième rangée et premiere colonne
cell = driver.find_element(By.XPATH, "//table[@name='BookTable']//tr[3]/td[1]")
print(cell.text)
# récupérer le texte de la troisième rangée et 3ieme colonne
cell = driver.find_element(By.XPATH, "//table[@name='BookTable']//tr[3]/td[3]")
print(cell.text)

cells = driver.find_elements(By.XPATH, "//table[@name='BookTable']//td")
for cel in cells:
    print(cel.text)
    if cel.text == "Learn Java":
        print("********* trouvée !")
        break

time.sleep(2)
driver.quit()
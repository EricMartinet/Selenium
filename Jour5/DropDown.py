from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://www.opencart.com/')
driver.find_element(By.XPATH, '//*[@id="navbar-collapse-header"]/div/a[2]' ).click()
#driver.find_element(By.XPATH, '//select[@name='country_id']/option')
dropDown_Country = driver.find_element(By.ID, "input-country")
country = Select(dropDown_Country)
#
# country.select_by_visible_text('Fiji')
# Pour les listes statiques : /index
# country.select_by_index(6)
all_options = country.options
print("Taille de la liste des options: ",len(all_options))
# Afficher toutes les options dans la console
# for option in all_options:
#     print(option.text)

for option in all_options:
    if option.text == "Fiji":
        option.click()
        break
driver.quit()
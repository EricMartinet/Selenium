# Test Case  EXERCICE 1   : AJOUTER UN ITEM SUR LE SITE D'AMAZON
# ------------------ PRE-CONDITIONS
# 1) Ouvrir le navigateur(chrome)
# 2) Naviguer vers l'url https://www.amazon.ca/
# 3) Saisir sur la zone de recherche le mot "selenium"
# 4) Cliquer sur le bouton loupe
# _________ ÉTAPES
# 5) S'assurer que la recherche a bien fonctionnée en trouvant 'results for "selenium"'
# 6) Cliquer sur le premier lien du produit
# 7) Vérifier que le texte encadré en rouge existe... mais il n'existe pas !
# 8) Cliquer sur le bouton radio achat unique
# 9) Cliquer sur le bouton add to cart
# 10) vérifier que le texte ajouté au panier est présent
# 11) Cliquer sur le bouton passer la commande
# 12) vérifier que le texte "Sign in" est présent
# _________ POST-CONDITIONS
# 13) Fermer le navigateur
import time

import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
# 1) Ouvrir le navigateur(chrome)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
time.sleep(2)
driver.maximize_window()
time.sleep(2)
# 2) Naviguer versL l'url https://www.amazon.ca/
driver.get('https://www.amazon.ca')
driver.save_screenshot("etape2.png")
time.sleep(8)
# 3) Saisir sur la zone de recherche le mot "selenium"
research_text = "selenium"
driver.find_element(By.ID, 'twotabsearchtextbox').send_keys(research_text)
driver.save_screenshot("etape3.png")
time.sleep(3)
# 4) Cliquer sur le bouton loupe
driver.find_element(By.XPATH, "//input[@id='nav-search-submit-button']").submit()
time.sleep(4)
# 5) S'assurer que la recherche a bien fonctionnée en trouvant 'results for "selenium"'
actual_search_text = driver.find_element(By.CSS_SELECTOR, "div[class='a-section a-spacing-small a-spacing-top-small']").text
expected_result = 'results for "'+research_text+'"'

driver.save_screenshot("etape5.png")
# assert expected_result in actual_search_text
if expected_result in actual_search_text:
    print("STEP5 PASSED")
else:
    print("STEP5 FAILED")
time.sleep(4)
product_name = "Pure Lab Vitamins - Copper Glycinate Mineral Supplement - 60 Vegan Caps - Essential for Coll…"
#xpath_item1 = "//*[text() = "+"'"+product_name+"']"
xpath_item1 = "//span[@class='a-truncate-cut'][contains(text(), "+"'"+product_name+"')]"

# 6) Cliquer sur le premier lien du produit
# driver.find_element(By.XPATH, "//span[@class='a-truncate-cut'][contains(text(),'Pure Lab Vitamins - Copper Glycinate Mineral Suppl')]").click()
driver.find_element(By.CSS_SELECTOR, 'body > div:nth-child(1) > div:nth-child(30) > div:nth-child(12) > div:nth-child(1) > div:nth-child(1) > span:nth-child(4) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(4) > div:nth-child(3) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > a:nth-child(1) > span:nth-child(1) > span:nth-child(2)').click()

# 7) Vérifier que le texte encadré en rouge existe... il n'existe pas ahahah
expected_back_label = 'Back to search results for "'+research_text+'"'
all_links = driver.find_elements(By.TAG_NAME, 'a')
time.sleep(5)
# print("nombre de liens :"+str(len(all_links)))
step7_OK = False
for link in all_links:
    try:
        print(link.get_attribute("innerText"))
        if expected_back_label in link.get_attribute("innerText"):
            print("le lien ayant pour libellé : '" + expected_result + '"' + ' est bien présent')
            step7_OK = True
    except selenium.common.exceptions.StaleElementReferenceException:
        continue
        #print("page pas finie d'être loadée?")
if step7_OK:
    print("STEP7 PASSED")
else:
    print("STEP7 FAILED")
    print("le lien ayant pour libellé : '" + expected_back_label + '"' + ' n\'est pas présent')
# Le lien n'existe pas, voir la copie d'écran
driver.save_screenshot("etape7.png")

# 8) Cliquer sur le bouton radio achat unique
driver.find_element(By.CSS_SELECTOR, '.a-icon.a-accordion-radio.a-icon-radio-inactive').click()
time.sleep(1)
driver.save_screenshot("etape8.png")

# 9) Cliquer sur le bouton add to cart
driver.find_element(By.XPATH, "//input[@id='add-to-cart-button']").submit()
driver.save_screenshot("etape9.png")
time.sleep(1)

# 10) vérifier que le texte ajouté au panier est présent
expected_confirmation = "Added to Cart"
actual_confirmation = driver.find_element(By.XPATH, "//span[@class='a-size-medium-plus a-color-base sw-atc-text a-text-bold']").text
driver.save_screenshot("etape10.png")
if expected_confirmation == actual_confirmation:
    print("STEP10 PASSED")
else:
    print("STEP10 FAILED")
# 11) Cliquer sur le bouton passer la commande
driver.find_element(By.XPATH, "//input[@name='proceedToRetailCheckout']").submit()
driver.save_screenshot("etape11.png")

# 12) vérifier que le texte "Sign in" est présent
expected_title_h1 = "Sign-In"
actual_title_h1 = driver.find_element(By.TAG_NAME, 'h1').text
driver.save_screenshot("etape12.png")
if expected_title_h1 == actual_title_h1:
    print("STEP12 PASSED")
else:
    print("STEP12 FAILED")
# 13) S'assurer que l'URL contient le mot signin
if driver.current_url.__contains__("signin"):
    print("STEP13 PASSED")
else:
    print("STEP13 FAILED")
# _________ POST-CONDITIONS
# 1) Fermer le navigateur
driver.quit()
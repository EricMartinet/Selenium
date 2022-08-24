# Test Case    EXERCICE 2 : VÉRIFIER L'ECHEC DE CONNECTION A LA PAGE LINKEDIN
# ------------------ PRE-CONDITIONS
# 1) Ouvrir le navigateur(firefox)
# 1B) Ouvrir la fenêtre en grand
# _________ ÉTAPES
# 2) Naviguer vers l'url https://www.LinkedIn.com/
# 3) Entrer le nom d'utilisateur fictif : "Fantomas"
# 4) Vérifier le titre de la page est == "LinkedIn: Log In or Sign Up"
# 5) Entrer le mauvais mot de passe : "who's bad?"
# 6) Cliquer sur le bouton "Sign in"
# 7) Attendre 5 secondes
# 8) Vérifier que le message d'erreur est == "Please enter a valid email address or mobile number."
# _________ POST-CONDITIONS
# 9) Fermer le navigateur
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

# 1) Ouvrir le navigateur(firefox)
driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
# 1B) Ouvrir la fenêtre en grand
driver.maximize_window()
# 2) Naviguer vers l'url https://www.LinkedIn.com/
driver.get("https://www.LinkedIn.com/")
driver.save_screenshot("step2.png")
time.sleep(4)
# 3) Vérifier le titre de la page  == "LinkedIn: Log In or Sign Up"
expected_title = "LinkedIn: Log In or Sign Up"
actual_title = driver.title
# assert expected_title == actual_title
if expected_title == actual_title:
    print("STEP3 PASSED")
else:
    print("STEP3 FAILED")
# 4) Entrer le nom d'utilisateur fictif : "Fantomas"
session_keys = "Fantomas"
driver.find_element(By.ID, 'session_key').send_keys(session_keys)
driver.save_screenshot('step3.png')
# 5) Entrer le mot de passe "who's bad?"
session_password = "who's bad?"
driver.find_element(By.XPATH, "//input[@id='session_password']").send_keys(session_password)
driver.save_screenshot("step4.png")
# 6) Cliquer sur le bouton "Sign in"
# //button[normalize-space()='Sign in']
driver.find_element(By.CSS_SELECTOR, ".sign-in-form__submit-button").submit()
# 7) Attendre 5 secondes
time.sleep(5)
# 8) Vérifier que le message d'erreur est : ""
expected_msg_error_log1 = "Please enter a valid email address or mobile number."
actual_msg_error_log1 = driver.find_element(By.CSS_SELECTOR, '.alert-content').text
print("Step7 - Message d'erreur :")
print(actual_msg_error_log1)
# assert expected_msg_error_log1 == actual_msg_error_log1
if expected_msg_error_log1 == actual_msg_error_log1:
    print("STEP7 PASSED")
else:
    print("STEP7 FAILED")
# _________ POST-CONDITIONS
# 9) Fermer le navigateur
driver.close()
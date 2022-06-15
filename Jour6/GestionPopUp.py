import time

from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()

# driver.get('https://the-internet.herokuapp.com/basic_auth')
# Pour contourner on entre le user et mot de passe entre https://  et l'adresse :
#           https://    user:password@   wwww.blablabla.com/truc/auth
driver.get('https://admin:admin@the-internet.herokuapp.com/basic_auth')

time.sleep(2)
driver.quit()
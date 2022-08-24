import time

from selenium import webdriver

# Création objet ChromeOptions
ops = webdriver.ChromeOptions()
# desactiver les notifications
ops.add_argument("--disable-notification")

driver = webdriver.Chrome(options=ops)
driver.maximize_window()
driver.get("https://whatmylocation.com/")

time.sleep(2)
driver.quit()

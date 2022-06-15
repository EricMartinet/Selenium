import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

driver.get('https://www.selenium.dev/selenium/docs/api/java/index.html?overview-summary.html')

# pour switcher vers le frame on peut le faire par name ou id
driver.switch_to.frame('packageListFrame')
time.sleep(2)
driver.find_element(By.LINK_TEXT, 'org.openqa.selenium').click()
time.sleep(2)

# retourner dans la page initiale
driver.switch_to.default_content()
driver.switch_to.frame('packageFrame')
time.sleep(2)
driver.find_element(By.XPATH, "//a/span[text()='WebDriver']").click()
time.sleep(2)

# Cliquer sur la page Help
driver.switch_to.default_content()
driver.switch_to.frame('classFrame')
driver.find_element(By.XPATH, "/html/body/header/nav/div[1]/div[1]/ul/li[8]/a")
time.sleep(2)

# ATTENTION PARFOIS IL EXISTE UN NESTED IFRAME
# driver.switch_to.parent_frame()
driver.quit()

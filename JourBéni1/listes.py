import time

from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By


driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
driver.maximize_window()
driver.get('https://selenium-python.readthedocs.io/locating-elements.html')
time.sleep(2)
#listes = driver.find_elements(By.XPATH, '//li')
listes = driver.find_elements(By.TAG_NAME, 'li')

for li in listes:
    print(li.text)

print('il existe ',len(listes),' listes')

driver.quit()




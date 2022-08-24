import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


#driver = webdriver.Chrome()
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
driver.get('https://wiki.ubuntu.com/')
driver.find_element(By.NAME, 'value').send_keys('Pingouin')
time.sleep(2)
driver.find_element(By.NAME, 'titlesearch').click()
time.sleep(2)
driver.quit()


# Login

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://demo.nopcommerce.com/")

driver.find_element(By.XPATH, "(//button[@type='submit'])[2]").click()
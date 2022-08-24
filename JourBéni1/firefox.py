from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
driver = webdriver.Firefox(service=Service(executable_path=GeckoDriverManager().install()))
driver.get("https://bdeb.qc.ca")
driver.maximize_window()
print(driver.title)
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://opensource-demo.orangehrmlive.com/')
time.sleep(2)

# Passage d'une fenetre à une autre : récupérer le handle
parent_window_id = driver.current_window_handle
# CDwindow-4D487DCF567E6547A8188C81895AB228
print(parent_window_id)
parent_window_url = driver.current_url
print(parent_window_url)
driver.find_element(By.LINK_TEXT, "OrangeHRM, Inc").click()
# récupérer la liste des fenetres ouvertes
windowS_id = driver.window_handles
# 1ere fenetre
parent_window_id = windowS_id[0]
# 2ieme fenetre
child_window_id = windowS_id[1]
print(parent_window_id)
print(child_window_id)
driver.switch_to.window(child_window_id)

child_window_url = driver.current_url
print(child_window_url)
child_title = driver.title
print(child_title)

######
# 2ieme approche
for winId in windowS_id:
    driver.switch_to.window(winId)
    if driver.title == child_title:
        driver.close()
time.sleep(2)
driver.quit()
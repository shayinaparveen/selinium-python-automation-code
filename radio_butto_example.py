import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.sugarcrm.com/au/request-demo/")
driver.maximize_window()
driver.find_element(By.ID, 'doi0').click()
print(driver.find_element(By.ID, 'doi0').is_selected())
time.sleep(4)
driver.find_element(By.ID, 'doi1').click()
print(driver.find_element(By.ID, 'doi0').is_selected())
print(driver.find_element(By.ID, 'doi1').is_selected())
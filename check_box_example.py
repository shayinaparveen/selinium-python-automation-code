import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.sugarcrm.com/au/request-demo/")
driver.maximize_window()
driver.find_element(By.ID, 'interest_market_c0').click()
time.sleep(2)
check = driver.find_element(By.ID, 'interest_market_c0').is_selected()
print(check)
check1 = driver.find_element(By.ID, 'interest_sell_c0').is_selected()
print(check1)


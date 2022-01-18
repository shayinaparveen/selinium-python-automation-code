from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://training.openspan.com/")
state_value = driver.find_element(By.ID, 'login_button').is_enabled()
print(state_value)
driver.find_element(By.CLASS_NAME, 'input_text').send_keys('almas')
driver.find_element(By.NAME, 'user_pass').send_keys('testing')
state_value1 = driver.find_element(By.ID, 'login_button').is_enabled()
print(state_value1)

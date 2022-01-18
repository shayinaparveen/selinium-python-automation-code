from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.w3schools.com/howto/howto_js_toggle_hide_show.asp")
element = driver.find_element(By.XPATH, "//div[@id='myDIV']").is_displayed()
print(element)
driver.find_element(By.XPATH, "//button[normalize-space()='Toggle Hide and Show']").click()
element1 = driver.find_element(By.XPATH, "//div[@id='myDIV']").is_displayed()
print(element1)

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.yatra.com/")
attr_value = driver.find_element(By.XPATH, "//input[contains(@value,'Search Flights')]").get_attribute("type")
print(attr_value)
driver.close()

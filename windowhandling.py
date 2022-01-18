from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


driver = webdriver.Chrome()
driver.get("https://yatra.com")
driver.maximize_window()
parent_handle = driver.current_window_handle
print(parent_handle)
driver.find_element(By.XPATH, "//a[@title='Web Check-in']//img[@class='conta iner large-banner']").click()
all_handles = driver.window_handles
print(all_handles)
for handle in all_handles:
    if handle != parent_handle:
        driver.switch_to.window(handle)
        driver.find_element(By.XPATH, "//span[normalize-space()='Singapore Airlines']").click()
        time.sleep(10)
        driver.close()
        time.sleep(10)
        break
driver.switch_to.window(parent_handle)
driver.find_element(By.XPATH, "//a[@title='Web Check-in']//img[@class='conta iner large-banner']").click()



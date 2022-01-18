import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://www.salesforce.com/in/form/signup/freetrial-sales/?d=jumbo1-btn-ft")
drop_down = driver.find_element(By.NAME, "UserTitle")
dd = Select(drop_down)
dd.select_by_index(1)
time.sleep(3)
dd.select_by_value("Customer_Service_Manager_AP")
time.sleep(3)
dd.select_by_visible_text("CxO / General Manager")
time.sleep(3)

# the deselect option will be working only in the multi list option
dd.deselect_by_index(1)
time.sleep(3)
dd.deselect_by_value("Customer_Service_Manager_AP")
time.sleep(3)
dd.deselect_by_visible_text("CxO / General Manager")
time.sleep(3)

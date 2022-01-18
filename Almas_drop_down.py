import time
from selenium import webdriver
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pdb


class drop_down():
    def dropdown(self):
        driver = webdriver.Chrome()
        driver.get("https://www.salesforce.com/in/form/signup/freetrial-sales/?d=jumbo1-btn-ft")
        driver.maximize_window()
        dd = driver.find_element(By.XPATH, "//select[@name = 'UserTitle']")
        dd = Select(dd)
        dd.select_by_index(1)
        time.sleep(5)
        dd.select_by_value("Customer_Service_Manager_AP")
        time.sleep(5)
        dd.select_by_visible_text("Developer / Software Engineer / Analyst")


cb = drop_down()
cb.dropdown()

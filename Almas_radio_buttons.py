import time
from selenium import webdriver
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pdb


class radio_buttons():
    def radiabuttons(self):
        driver = webdriver.Chrome()
        driver.get("https://www.sugarcrm.com/au/request-demo/")
        driver.maximize_window()
        wait = WebDriverWait(driver, 60)
        wait.until(EC.element_to_be_clickable((By.ID, "doi0")))
        radio = driver.find_element(By.ID, "doi0").is_selected()
        print(radio)
        # pdb.set_trace()
        first = driver.find_element(By.ID, "doi0")
        first.click()
        radio1 = driver.find_element(By.ID, "doi0").is_selected()
        print(radio1)

        wait.until(EC.element_to_be_clickable((By.ID, "doi1")))
        radio2 = driver.find_element(By.ID, "doi1").is_selected()
        print(radio2)
        # pdb.set_trace()
        second = driver.find_element(By.ID, "doi1")
        second.click()
        radio3 = driver.find_element(By.ID, "doi0").is_selected()
        print(radio3)


cb = radio_buttons()
cb.radiabuttons()

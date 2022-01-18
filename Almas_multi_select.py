import time
from selenium import webdriver
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pdb


class multi_select():
    def multiselect(self):
        driver = webdriver.Chrome()
        driver.get("file:///C:/Users/ashaikha/Desktop/multidrop.html")
        driver.maximize_window()
        time.sleep(5)
        elem = driver.find_element(By.NAME, "Mobdevices")
        ms = Select(elem)
        ms.select_by_index(0)
        time.sleep(5)
        ms.select_by_value("1")
        time.sleep(5)
        ms.select_by_visible_text("BlackBerry")
        time.sleep(5)
        ms.deselect_by_index(0)
        time.sleep(5)
        ms.deselect_by_value("1")
        time.sleep(5)
        ms.deselect_by_visible_text("BlackBerry")
        time.sleep(5)
        ms.deselect_all()




cb = multi_select()
cb.multiselect()

from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class cs_name():
    def csname(self):
        driver = webdriver.Chrome()
        driver.get("https://training.rcvacademy.com/")
        driver.find_element(By.XPATH, "//a[contains(text(),'Sign up now')]").click()
        driver.find_element(By.XPATH, "//a[contains(text(),'Sign up now')]").click()


cs = cs_name()
cs.csname()

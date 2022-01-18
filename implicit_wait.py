import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class implicit_wait():

    def implicitwait(self):
        driver = webdriver.Chrome()
        driver.get("https://login.salesforce.com/?locale=in")
        driver.implicitly_wait(10)
        driver.find_element(By.ID, "useaarname").send_keys("almas")
        driver.find_element(By.ID, "password").send_keys("mohamed")


iw = implicit_wait()
iw.implicitwait()

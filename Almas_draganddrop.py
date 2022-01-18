import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.service import Service
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager


class drag_drop:

    def dragdrop(self):
        # driver = webdriver.Chrome()

        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://jqueryui.com/droppable/")
        driver.maximize_window()
        driver.switch_to.frame(driver.find_element(By.XPATH, "//iframe[@class='demo-frame']"))
        source = driver.find_element(By.ID, "draggable")
        destination = driver.find_element(By.ID, "droppable")
        ActionChains(driver).drag_and_drop(source, destination).perform()
        # ActionChains(driver).drag_and_drop_by_offset(source, 419, 238).perform()


dd = drag_drop()
dd.dragdrop()

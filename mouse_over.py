import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class demo_mouse_hover():

    def mouse_hover(self):
        driver = webdriver.Chrome()
        driver.get("https://www.yatra.com/")
        driver.maximize_window()
        # more = driver.find_element(By.XPATH, "//span[@class='more-arr']")
        # action_chain = ActionChains(driver)
        # action_chain.move_to_element(more).perform()
        # time.sleep(5)
        # driver.find_element(By.XPATH, "//span[normalize-space()='Xplore']").click()
        # time.sleep(5)

        driver.maximize_window()
        more = driver.find_element(By.XPATH, "//a[contains(text(),'My Account')]")
        time.sleep(5)
        action_chains = ActionChains(driver)
        action_chains.move_to_element(more).perform()
        driver.find_element(By.XPATH, "//a[@id='signInBtn']").click()



ja = demo_mouse_hover()
ja.mouse_hover()

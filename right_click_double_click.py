import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class rightclick_doubleclick():

    def right_double(self):
        driver = webdriver.Chrome()
        driver.get("https://demo.guru99.com/test/simple_context_menu.html")
        driver.maximize_window()
        # elem1 = driver.find_element(By.XPATH, "//span[@class='context-menu-one btn btn-neutral']")
        # action_chains = ActionChains(driver)
        # action_chains.context_click(elem1).perform()
        # time.sleep(5)
        # copy = driver.find_element(By.XPATH,
        #                            "//li[@class='context-menu-item context-menu-icon context-menu-icon-copy']")
        # copy.click()
        # time.sleep(5)

        elem3 = driver.find_element(By.XPATH, "//button[normalize-space()='Double-Click Me To See Alert']")
        action_chains = ActionChains(driver)
        action_chains.double_click(elem3).perform()
        time.sleep(5)


ja = rightclick_doubleclick()
ja.right_double()

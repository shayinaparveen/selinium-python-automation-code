import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class slider_bar:

    def slidebar(self):
        driver = webdriver.Chrome()
        driver.get("https://www.snapdeal.com/search?keyword=mobile%20phones&sort=rlvncy")
        driver.maximize_window()
        elem1 = driver.find_element(By.XPATH, "//a[contains(@class, 'left-handle')]")
        elem2 = driver.find_element(By.XPATH, "//a[contains(@class, 'right-handle')]")
        ActionChains(driver).drag_and_drop_by_offset(elem1, 60, 0).perform()
        time.sleep(5)
        ActionChains(driver).drag_and_drop_by_offset(elem2, -60, 0).perform()
        time.sleep(5)
        # ActionChains(driver).move_to_element(elem1).pause(1).click_and_hold(elem1).move_by_offset(60, 0).release().perform()
        # ActionChains(driver).click_and_hold(elem1).pause(1).move_by_offset(60, 0).release().perform()


sb = slider_bar()
sb.slidebar()

from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class text_element():
    def txelement(self):
        driver = webdriver.Chrome()
        driver.get("https://www.yatra.com/")
        t=driver.find_element(By.XPATH, "//div[@class='ripple-parent search-height demo-icon icon-go']//input[@id='BE_flight_flsearch_btn']")
        print(t.text)
        list_a = driver.find_element(By.TAG_NAME, 'a')
        print(list_a.text)


cs = text_element()
cs.txelement()

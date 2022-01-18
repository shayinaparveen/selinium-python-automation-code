import time
from selenium import webdriver
from selenium.webdriver.common.by import By


class check_box():
    def checkbox(self):
        driver = webdriver.Chrome()
        driver.get("https://www.sugarcrm.com/au/request-demo/")
        check = driver.find_element(By.XPATH,"//input[@name ='interest_market_c']").is_selected()
        print(check)
        driver.find_element(By.XPATH,"//input[@name ='interest_market_c']").click()
        check_1 = driver.find_element(By.XPATH, "//input[@name ='interest_market_c']").is_selected()
        print(check_1)
        time.sleep(5)


cb = check_box()
cb.checkbox()

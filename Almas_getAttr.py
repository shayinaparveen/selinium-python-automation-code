from selenium import webdriver
from selenium.webdriver.common.by import By


class get_attr():
    def getattr(self):
        driver = webdriver.Chrome()
        driver.get("https://yatra.com")
        driver.maximize_window()
        attr_value = driver.find_element(By.XPATH, "//input[contains(@value,'Search Flights')]").get_attribute("type")
        print(attr_value)
        driver.close()


ga = get_attr()
ga.getattr()

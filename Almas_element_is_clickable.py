from selenium import webdriver
from selenium.webdriver.common.by import By


class element_clickable():
    def elementclickable(self):
        driver = webdriver.Chrome()
        driver.get("https://training.openspan.com/login")
        driver.maximize_window()
        elem_state = driver.find_element(By.ID, "login_button").is_enabled()
        print(elem_state)
        driver.find_element(By.ID, "user_name").send_keys("Almas")
        driver.find_element(By.ID, "password").send_keys("Mohamed")
        after = driver.find_element(By.ID, "login_button").is_enabled()
        print(after)
        driver.find_element(By.ID, "login_button").click()


ec = element_clickable()
ec.elementclickable()

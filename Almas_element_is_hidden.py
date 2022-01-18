from selenium import webdriver
from selenium.webdriver.common.by import By


class element_hidden():
    def elementhidden(self):
        driver = webdriver.Chrome()
        driver.get("https://www.w3schools.com/howto/howto_js_toggle_hide_show.asp")
        driver.maximize_window()
        hid_elem = driver.find_element(By.XPATH, "//div[contains(text(), 'Click the button!')]").is_displayed()
        print(hid_elem)
        driver.find_element(By.XPATH, "//button[contains(text(), 'Toggle Hide and Show')]").click()
        hid_elem1 = driver.find_element(By.XPATH, "//div[contains(text(), 'Click the button!')]").is_displayed()
        print(hid_elem1)

ec = element_hidden()
ec.elementhidden()

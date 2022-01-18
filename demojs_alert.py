import time
from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class demo_js_alert():

    def js_alert(self):
        driver = webdriver.Chrome()
        driver.get("https://www.w3schools.com/js/tryit.asp?filename=tryjs_prompt")
        driver.maximize_window()
        # driver.execute_script("window.open('https://training.rcvacademy.com/', '_self');")
        driver.switch_to.frame("iframeResult")
        time.sleep(6)
        # driver.find_element(By.XPATH, "//button[contains(text(),'Try it')]").click()
        # driver.switch_to.alert.accept()
        # time.sleep(2)
        # driver.find_element(By.XPATH, "//button[contains(text(),'Try it')]").click()
        # driver.switch_to.alert.dismiss()
        # time.sleep(2)
        # driver.find_element(By.XPATH, "//button[contains(text(),'Try it')]").click()
        # t = driver.switch_to.alert.text
        # print(t)
        # driver.switch_to.alert.send_keys("Almas Mohamed")
        # driver.switch_to.alert.accept()
        # time.sleep(2)

        driver.find_element(By.XPATH, "//button[contains(text(),'Try it')]").click()
        Alert(driver).accept()
        time.sleep(2)
        driver.find_element(By.XPATH, "//button[contains(text(),'Try it')]").click()
        Alert(driver).dismiss()
        time.sleep(2)
        driver.find_element(By.XPATH, "//button[contains(text(),'Try it')]").click()
        t = Alert(driver).text
        print(t)
        driver.switch_to.alert.send_keys("Almas Mohamed")
        Alert(driver).accept()
        time.sleep(2)



ja = demo_js_alert()
ja.js_alert()

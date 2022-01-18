import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By


class handling_alerts():
    def handlingalerts(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--incognito')
        driver = webdriver.Chrome(options=options)
        driver.get("https://www.w3schools.com/js/tryit.asp?filename=tryjs_prompt")
        driver.maximize_window()
        driver.switch_to.frame("iframeResult")
        driver.find_element(By.XPATH, "//button[contains(text(),'Try it')]").click()
        driver.switch_to.alert.accept()
        time.sleep(2)
        driver.find_element(By.XPATH, "//button[contains(text(),'Try it')]").click()
        driver.switch_to.alert.dismiss()
        time.sleep(2)
        driver.find_element(By.XPATH, "//button[contains(text(),'Try it')]").click()
        t = driver.switch_to.alert.text
        print(t)
        driver.switch_to.alert.send_keys("Almas Mohamed")
        driver.switch_to.alert.accept()
        time.sleep(2)

        # Alert(driver).accept()
        # Alert(driver).dismiss()
        # Alert(driver).send_keys()




ha = handling_alerts()
ha.handlingalerts()

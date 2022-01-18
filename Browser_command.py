from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class browser_command():
    def bro(self):
        driver = webdriver.Chrome()
        driver.get("https://training.rcvacademy.com/")
        print(driver.current_url)
        time.sleep(3)
        print(driver.title)
        time.sleep(3)
        driver.maximize_window()
        time.sleep(3)
        driver.refresh()
        time.sleep(3)
        driver.find_element(By.XPATH, "//a[normalize-space()='BACK TO MAIN WEBSITE']").click()
        driver.back()
        time.sleep(3)
        driver.forward()
        time.sleep(3)
        driver.fullscreen_window()
        time.sleep(3)
        driver.minimize_window()
        time.sleep(3)
        driver.close()
        time.sleep(3)
        driver.quit()
        time.sleep(3)


bc = browser_command()
bc.bro()

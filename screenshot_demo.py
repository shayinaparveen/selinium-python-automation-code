import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class demo_screenshot():
    def demo_screen(self):
        driver = webdriver.Chrome()
        driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")
        cont = driver.find_element(By.XPATH, "//button[@id='login-continue-btn']")
        cont.click()
        cont.screenshot(".\\test.png")
        time.sleep(3)
        driver.get_screenshot_as_file(".\\test1.png")
        time.sleep(3)
        driver.save_screenshot(".\\test2.png")


screen = demo_screenshot()
screen.demo_screen()
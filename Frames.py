from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


class demo_iframes():
    def dmo_fr(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_iframe_frameborder_css")
        driver.switch_to.frame(driver.find_element(By.XPATH, "//iframe[@id = 'iframeResult']"))
        driver.switch_to.frame(0)
        driver.find_element(By.XPATH, "//a[@id= 'navbtn_menu']").click()
        time.sleep(10)
        driver.switch_to.default_content()


df = demo_iframes()
df.dmo_fr()

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class demo_jscript():

    def demojs(self):
        driver = webdriver.Chrome()
        # driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")
        driver.execute_script("window.open('https://training.rcvacademy.com/', '_self');")
        time.sleep(8)
        demo_element = driver.execute_script("return document.(getElementsByTagName('p')[1]);")
        driver.execute_script("argument[0].click();", demo_element)


djs = demo_jscript()
djs.demojs()

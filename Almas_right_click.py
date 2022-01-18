import time
from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By


class right_click():
    def rightclick(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--incognito')
        driver = webdriver.Chrome(options=options)
        driver.get("https://demo.guru99.com/test/simple_context_menu.html")
        driver.maximize_window()
        r = driver.find_element(By.XPATH, "//span[contains(text(),'right click me')]")
        action = ActionChains(driver)
        action.context_click(r).perform()
        time.sleep(5)
        c = driver.find_element(By.XPATH, "//span[contains(text(),'Copy')]")
        c.click()
        time.sleep(5)
        p = Alert(driver).text
        print(p)
        Alert(driver).accept()

        d = driver.find_element(By.XPATH, "//button[contains(text(),'Double-Click Me To See Alert')]")
        action.double_click(d).perform()
        time.sleep(5)
        do = Alert(driver).text
        print(do)
        Alert(driver).accept()


rc = right_click()
rc.rightclick()

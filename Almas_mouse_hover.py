import time
from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By


class mouse_hover():
    def mousehover(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--incognito')
        driver = webdriver.Chrome(options=options)
        driver.get("https://yatra.com")
        more = driver.find_element(By.XPATH, "//span[@class = 'more-arr']")
        action = ActionChains(driver)
        action.move_to_element(more).perform()
        driver.find_element(By.XPATH, "//a[@title='Monuments']").click()
        time.sleep(5)


mh = mouse_hover()
mh.mousehover()

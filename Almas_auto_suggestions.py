import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


class auto_sug():
    def autosug(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--incognito')
        driver = webdriver.Chrome(options=options)
        driver.get("https://yatra.com")
        driver.maximize_window()
        # driver.implicitly_wait(20)
        depart_from = driver.find_element(By.XPATH, "//input[@id='BE_flight_origin_city']")
        depart_from.click()
        depart_from.send_keys("New Delhi")
        depart_from.send_keys(Keys.ENTER)
        depart_to = driver.find_element(By.XPATH, "//input[@class= 'required_field cityPadLeft ac_input dest_ac']")
        time.sleep(5)
        depart_to.clear()
        time.sleep(5)
        depart_to.send_keys("New")
        search_results = driver.find_elements(By.XPATH, "//div[@class = 'viewport']/child::div/child::div/child::li")
        print(len(search_results))
        time.sleep(5)
        for result in search_results:
            print(result.text)

            if "Sanganeer" in result.text:
                result.click()
                time.sleep(4)
                break




asug = auto_sug()
asug.autosug()

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class demo_auto_select():
    def demo_select(self):
        driver = webdriver.Chrome()
        driver.get("https://www.yatra.com/")
        # going_from = driver.find_element(By.XPATH, "//input[@id='BE_flight_origin_city']")
        # going_from.click()
        # time.sleep(3)
        # going_from.send_keys("New Delhi")
        # time.sleep(3)
        # going_from.send_keys(Keys.ENTER)
        # time.sleep(3)
        # going_to = driver.find_element(By.XPATH, "//input[@id='BE_flight_arrival_city']")
        # time.sleep(3)
        # going_to.send_keys("New")
        # time.sleep(4)
        # search_results = driver.find_elements(By.XPATH, "//div[@class='viewport']//div[1]/li")
        # print(len(search_results))
        # for result in search_results:
        #     if "New York (JFK)" in result.text:
        #         result.click()
        #         time.sleep(4)
        #         break

        depart = driver.find_element(By.XPATH, "//input[@id='BE_flight_origin_date']")
        depart.click()
        time.sleep(3)
#        driver.find_element(By.XPATH, "//td[@id='18/01/2022']").click()

        all_dates = driver.find_elements(By.XPATH, "//div[@id = 'monthWrapper']//tbody//td[@class!='inActiveTD']")
        for date in all_dates:
            if date.get_attribute("data-date") == "18/01/2022":
                date.click()
                time.sleep(10)
                break


dautoselect = demo_auto_select()
dautoselect.demo_select()

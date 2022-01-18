import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class fluent_wait():
    def f_wait(self):
        driver = webdriver.Chrome()
        driver.get("https://www.yatra.com/")
        driver.maximize_window()
        going_from = driver.find_element(By.XPATH, "//input[@id='BE_flight_origin_city']")
        going_from.click()
        going_from.send_keys("New Delhi")
        going_from.send_keys(Keys.ENTER)
        wait = WebDriverWait(driver, 10)
        wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='BE_flight_arrival_city']")))
        # going_to = driver.find_element(By.XPATH, "//input[@id='BE_flight_arrival_city']")
        going_to = driver.find_element(By.XPATH, "//input[@id='BE_flight_arrival_city']")
        going_to.click()
        going_to.send_keys("New")
        search_results = driver.find_elements(By.XPATH, "//div[@class='viewport']//div[1]/li")
        print(len(search_results))

        for result in search_results:
            print(result.text)
            if "New York (JFK)" in result.text:
                result.click()
                break

        wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='BE_flight_origin_date']"))).click()

        # driver.find_element(By.XPATH, "//td[@id='18/01/2022']").click()
        # wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@id = 'monthWrapper']//tbody//td["
        #                                                  "@class!='inActiveTD']")))
        all_dates = driver.find_elements(By.XPATH, "//div[@id = 'monthWrapper']//tbody//td["
                                                   "@class!='inActiveTD']")

        # all_dates = driver.find_elements(By.XPATH, "//div[@id = 'monthWrapper']//tbody//td[@class!='inActiveTD']")
        for date in all_dates:
            if date.get_attribute("data-date") == "18/01/2022":
                date.click()
                break
        driver.find_element(By.XPATH, "//input[@value='Search Flights']").click()


fw = fluent_wait()
fw.f_wait()

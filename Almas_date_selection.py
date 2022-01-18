import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


class date_sel():
    def datesel(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--incognito')
        driver = webdriver.Chrome(options=options)
        driver.get("https://yatra.com")
        driver.maximize_window()
        dd = driver.find_element(By.XPATH, "//input[@id='BE_flight_origin_date']")
        dd.click()
        dd.screenshot(".\\date.png")
        driver.save_screenshot(".\\date1.png")


        time.sleep(5)
        all_dates = driver.find_elements(By.XPATH, "//div[@id = 'monthWrapper']//tbody//td[@class != 'inActiveTD']")
        # print(all_dates)
        # with open("dates.text", "w") as f:
        #     for date in all_dates:
        #         f.write(date.text)

        for date in all_dates:
            if date.get_attribute("data-date") == "21/01/2022":
                driver.get_screenshot_as_file(".\\date3.png")
                date.click()
                time.sleep(4)
                break


ds = date_sel()
ds.datesel()

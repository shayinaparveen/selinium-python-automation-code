from selenium import webdriver
from selenium.webdriver.common.by import By


class get_text():
    def gettext(self):
        driver = webdriver.Chrome()
        driver.get("https://training.rcvacademy.com/")
        l = driver.find_element(By.XPATH, "//a[contains(text(),'Sign up now')]")
        print(str(l.text))


cn = get_text()
cn.gettext()

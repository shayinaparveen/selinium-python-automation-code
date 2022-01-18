from selenium import webdriver
from selenium.webdriver.common.by import By


class list_elements():
    def list_of_elements(self):
        driver = webdriver.Chrome()
        driver.get("https://yatra.com")
        l = driver.find_elements(By.TAG_NAME, "a")
        for i in l:
            print(i.text)

        with open("list.txt", "w") as f:
            for i in l:
                f.write(str(i.text))

        with open("list.txt", "r") as fr:
            fr.readline()
        n = 5
        with open("list.txt", "r") as file:
            for x in range(n):
                lines = next(file)
                print(str(lines))


le = list_elements()
le.list_of_elements()

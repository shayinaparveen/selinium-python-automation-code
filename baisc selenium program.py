# from selenium import webdriver
from selenium.webdriver import DesiredCapabilities, ActionChains
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

# driver = webdriver.Chrome()
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument("--incognito")
# driver = webdriver.Chrome(chrome_options=chrome_options)
options = webdriver.ChromeOptions()
options.add_argument('--incognito')
driver = webdriver.Chrome(options=options)
# options.add_argument('headless')
# driver = webdriver.Chrome(options=options)
driver.maximize_window()
# driver.get('https://google.com')
driver.get("http://demostore.supersqa.com/my-account/")
# assert "Python" in driver.title
# element = driver.find_element(By.XPATH, "//a[@data-action= 'sign in']")

driver.find_element(By.XPATH, "//input[@name='username']").send_keys("almas.mohamed23786@gmail.com")
driver.find_element(By.XPATH, "//input[@name='password']").send_keys("Shayina12!!")
driver.find_element(By.XPATH, "//button[@name='login']").click()
assert "No results found." not in driver.page_source
input_element = driver.find_element(By.XPATH, "//div[@id = 'page']")
input_element.send_keys(Keys.ARROW_DOWN)
# driver.close()


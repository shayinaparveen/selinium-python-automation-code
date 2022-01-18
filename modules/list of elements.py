from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://yatra.com")
list_a = driver.find_elements(By.TAG_NAME, 'a')
print(len(list_a))
# f = open("a_tags.txt", "w")
# for i in list_a:
#     f.write(str(i.text) + "\n")
# f.close()
with open("keywords.txt" , 'w') as f:
    for i in list_a:
        f.write(str(i.text) + "\n")

with open("keywords.txt" , 'r') as fr:
    print(fr.readline())
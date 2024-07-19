import requests

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://www.deadlinkcity.com/")
driver.maximize_window()

alllinks = driver.find_elements(By.TAG_NAME, 'a')
count = 0

for link in alllinks:
    url = link.get_attribute('href')
    try:
        res = requests.head(url)
    except:
        None

    if res.status_code >= 400:
        print("thins is broken lnk")
        count + 1
    else:
        print(url, "is not broken")
print("total nukber of brokne  links", count)

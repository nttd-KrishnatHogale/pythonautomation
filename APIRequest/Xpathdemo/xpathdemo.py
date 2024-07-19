from selenium import webdriver
import time
from selenium.webdriver.common.by import By

# from selenium.webdriver.chrome.service import Service
# from test.test_lib2to3.support import driver
# chrome_service = Service("C:\chromedriver\chromedriver-win64\chromedriver.exe")

# driver = webdriver.Chrome(service=chrome_service)
driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://opensource-demo.orangehrmlive.com/")
time.sleep(5)
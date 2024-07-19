from selenium.webdriver.common.by import By

import XLUtils
from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://demo.guru99.com/selenium/newtours/")
driver.maximize_window()

path = "C:/Users/262164/Desktop/Login1.xlsx"

rows = XLUtils.getrowcount(path, 'Sheet1')


for r in range(2,rows+1):
    username = XLUtils.ReadData(path,"Sheet1", r ,1)
    password = XLUtils.ReadData(path,"Sheet1", r ,2)

    driver.find_element(By.NAME, "userName").send_keys(username)
    driver.find_element(By.NAME, "password").send_keys(password)
    driver.find_element(By.NAME, "submit").click()

    if driver.title == "Find a Flight: Mercury Tours:":
        print("test is passed")
        XLUtils.writeData(path, "Sheet1", r, 3, "test passed")
    else:
        print("test is failed")
        XLUtils.writeData(path, "Sheet1", r, 3, "test failed")

    driver.find_element(By.LINK_TEXT, "Home").click()

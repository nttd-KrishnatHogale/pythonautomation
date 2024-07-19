import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://mypage.rediff.com/login/dologin")
driver.maximize_window()

driver.find_element(By.XPATH,"//input[@value='Login']").click()
time.sleep(2)
myalert = driver.switch_to.alert.accept()
# myalert.accept()

driver.close()
# print(alertwindow.text)
# alertwindow.send_keys("welcome")

# alertwindow.accept()

# alertwindow.dismiss()
# time.sleep(2)

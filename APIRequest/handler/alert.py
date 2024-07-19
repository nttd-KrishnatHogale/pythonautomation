import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
driver.find_element(By.XPATH,"/html/body/div[4]/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div/div[4]/div[3]/div/aside/div/div[3]/div[1]/button[1]").click()
time.sleep(2)
# try:
    # wait.until(EC.alert_is_present())
    # driver.switch_to.alert.accept()
alert = driver.switch_to.alert
alert.accept()
# except:
#     print("error")
# driver.switch_to.alert().dismiss()
# go tolinl
# login is present or not
# try to login
# check for msg
# displyed msg == our msg
# login failed
# exit
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
url = "https://demo.nopcommerce.com/"
driver.get(url)
driver.maximize_window()

# verify login is present or not
login = driver.find_element(By.XPATH, "//a[normalize-space()='Log in']")
if login.text != "Log in":
    print("user is logged in")
else:
    print("login option is present")

# try to login
Moving_To_Login = driver.find_element(By.XPATH, "//a[normalize-space()='Log in']")
Moving_To_Login.click()
time.sleep(5)

#email & password enter
email = driver.find_element(By.XPATH, "//input[@id='Email']")
email.send_keys("123@abc.com")
password = driver.find_element(By.XPATH, "//input[@id='Password']")
password.send_keys("123@abc")
submit = driver.find_element(By.XPATH,"//button[normalize-space()='Log in']")
submit.click()

time.sleep(5)


myaccouint = driver.find_element(By.XPATH,"//a[@class='ico-account']")
if myaccouint.text != "My account":
    print("User Not logged in")
else:
    print("user Logged in")

driver.quit()
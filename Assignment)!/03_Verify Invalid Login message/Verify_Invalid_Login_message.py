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
email.send_keys("123")

time.sleep(5)

loginbutton = driver.find_element(By.XPATH,"//button[normalize-space()='Log in']")
loginbutton.click()
emailError = driver.find_element(By.XPATH, "//span[@id='Email-error']")
time.sleep(10)

if emailError.text == "Please enter a valid email address.":
    print(emailError.text)
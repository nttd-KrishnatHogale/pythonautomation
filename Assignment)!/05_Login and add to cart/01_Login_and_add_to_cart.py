# login present or not
# login
#

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
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


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

# time.sleep(5)

# click on electrinic camera
electronicImage = driver.find_element(By.XPATH, "//img[@title='Show products in category Electronics']")
electronicImage.click()
time.sleep(3)

# select camera& photo
selctcamera = driver.find_element(By.XPATH,"//img[@title='Show products in category Camera & photo']")
selctcamera.click()

# selectlowtohigh = driver.find_element(By.XPATH, "//option[@value='10']")
selectlowtohigh = Select(driver.find_element(By.ID,"products-orderby"))
print(type(selectlowtohigh))
selectlowtohigh.select_by_value("10")
time.sleep(4)

# Add to cart
addTocart = driver.find_element(By.XPATH,"//div[@class='item-grid']//div[1]//div[1]//div[2]//div[3]//div[2]//button[1]")
addTocart.click()


# time.sleep(4)


driver.quit()
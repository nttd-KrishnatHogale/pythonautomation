import time

from  selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://en.wikipedia.org/wiki/MS_Dhoni")
driver.maximize_window()

#scroll down by  pixel
# driver.execute_script("window.scrollBy(0,1000)","")

# scroll down page till element is visible
# flag = driver.find_element(By.XPATH,"//span[@id='Final_years_and_retirement']")
# driver.execute_script("arguments[0],scrollIntoView();", flag)

driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")

time.sleep(10)
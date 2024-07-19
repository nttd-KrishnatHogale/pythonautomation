import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://jqueryui.com/datepicker/")
driver.maximize_window()
driver.switch_to.frame(0)
# driver.find_element(By.XPATH, "//*[@id='datepicker']").send_keys("06/30/2022")

year = "2020"
month = "March"
date = "27"

driver.find_element(By.XPATH, "//*[@id='datepicker']").click()

while True:
    mon =driver.find_element(By.XPATH, "//span[@class='ui-datepicker-month']").text
    yr = driver.find_element(By.XPATH,"//span[@class='ui-datepicker-year']").text

    if mon == month and yr == year:
        break
    else:
        # driver.find_element(By.XPATH, "//*[@id='ui-datepicker-div']/div/a[2]/span").click() //for forward move
        driver.find_element(By.XPATH, "//*[@id='ui-datepicker-div']/div/a[1]/span").click() #for previous moves


#select date
dates = driver.find_elements(By.XPATH,"//div[@id='ui-datepicker-div']//table/tbody/tr/td/a")

for ele in dates:
    if ele.text==date:
        ele.click()
        break
# time.sleep(10)
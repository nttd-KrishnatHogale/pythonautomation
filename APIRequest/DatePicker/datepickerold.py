import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


driver = webdriver.Chrome()
driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
# Date of birth
driver.find_element(By.XPATH,"//input[@id='dob']").click()
# moth selection
mnth = driver.find_element(By.XPATH,"//select[@data-handler='selectMonth']")
datepicker_month = Select(mnth)
datepicker_month.select_by_visible_text("Mar")
# year selection

year = driver.find_element(By.XPATH,"//select[@data-handler='selectYear']")
datepicker_year = Select(year)
datepicker_year.select_by_visible_text("2000")

alldates = driver.find_elements(By.XPATH, "//div[@id='ui-datepicker-div']//table/tbody/tr/td/a")

for date in alldates:
    if date.text == "27":
        date.click()
        break

time.sleep(5)
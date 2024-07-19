import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

# driver.find_element(By.XPATH,"//input[@id='sunday']")

checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox' and contains(@id,'day')]")

# time.sleep(10)
print(len(checkboxes))

# for i in range(len(checkboxes)):
#     checkboxes[i].click()


# for i in checkboxes:
#     i.click()


# for i in checkboxes:
#     weekname = i.get_attribute('id')
#     if weekname == 'sunday' or weekname == 'monday':
#         i.click()


# for i in range(len(checkboxes)-2, len(checkboxes)):
#     checkboxes[i].click()

# for i in range(len(checkboxes)):
#     if i<2:
#         checkboxes[i].click()

for checkbox in checkboxes:
    if checkbox.is_selected():
        checkbox.click()
time.sleep(5)
driver.quit()

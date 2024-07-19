import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
url = "https://demo.nopcommerce.com/"
driver.get(url)
driver.maximize_window()

driver.find_element(By.XPATH, "(//button[normalize-space()='Search'])[1]").send_keys(Keys.RETURN)

try:
    WebDriverWait(driver,20).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    alttext = alert.text
    alert.accept()
    print(alttext)
finally:
    driver.quit()

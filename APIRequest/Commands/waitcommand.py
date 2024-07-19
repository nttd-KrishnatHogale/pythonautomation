import time
# from telnetlib import EC

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



driver = webdriver.Chrome()
# driver.implicitly_wait(10)
# //explicite wait
myWait = WebDriverWait(driver, 10)

driver.get("https://www.google.com/")
driver.maximize_window()

searchbox = driver.find_element(By.NAME, 'q')
searchbox.send_keys("selenium")
searchbox.submit()
# time.sleep(5)

searchlink = myWait.until(EC.presence_of_element_located((By.XPATH,"//h3[text()='Selenium']")))

searchlink.click()
# driver.find_element().click()
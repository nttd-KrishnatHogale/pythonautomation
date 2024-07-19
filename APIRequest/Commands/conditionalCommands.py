from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()

search_box = driver.find_element(By.XPATH,"//*[@id='small-searchterms']")
print("Status ", search_box.is_displayed())
print("Enalblesd ", search_box.is_enabled())

driver.quit()
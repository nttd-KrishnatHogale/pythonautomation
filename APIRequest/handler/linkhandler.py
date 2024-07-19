from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()

# driver.find_element(By.LINK_TEXT, "Digital downloads").click()
# driver.find_element(By.PARTIAL_LINK_TEXT,"Digital").click()

link = driver.find_elements(By.XPATH, '//a')
print("total links", len(link))

for li in link:
    print(li.text)
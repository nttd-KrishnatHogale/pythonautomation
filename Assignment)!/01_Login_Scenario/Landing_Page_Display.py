import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome()
url = "https://demo.nopcommerce.com/"
driver.get(url)
driver.maximize_window()
def login():
    # welcome msg is present or not
    welcomeMSg = driver.find_element(By.XPATH, "//h2[normalize-space()='Welcome to our store']")
    # print(welcomeMSg.text)
    if welcomeMSg.text == "Welcome to our store":
        print("Welcome to our store is present")
    else:
        print("not present")
    #  is search box avialble or not
    # find serach box and enter T-Shirt
    searchbox = driver.find_element(By.XPATH, "(//input[@id='small-searchterms'])[1]")
    searchbox.send_keys("T-Shirt")
    driver.find_element(By.XPATH, "(//button[normalize-space()='Search'])[1]").send_keys(Keys.RETURN)
    # time.sleep(2)
    try:
        product_grid = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "product-grid")))

        if product_grid:
            print("Product grid is present so items are available")
        else:
            print("No items Available")
    finally:
        driver.quit()
login()
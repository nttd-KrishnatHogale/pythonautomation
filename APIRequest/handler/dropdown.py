# from select import select
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


driver = webdriver.Chrome()
# driver.get("https://www.opencart.com/index.php?route=account/register")
driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()

# driver.implicitly_wait(30)

# drpcountry = Select(driver.find_element(By.XPATH, "//select[@id='input-country']"))
selsectcurrency = Select(driver.find_element(By.XPATH, "//select[@id='customerCurrency']"))
selsectcurrency.select_by_visible_text("Euro")
# drpcountry.select_by_visible_text("India")
# drpcountry.select_by_value("10")
# drpcountry.select_by_index(13)
time.sleep(10)
# alloptions= drpcountry.options
# print("tootle number of options: ",len(alloptions))


# for opt in alloptions:
#     print(opt.text)
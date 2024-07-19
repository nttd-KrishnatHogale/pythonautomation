from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()

windowid = driver.current_window_handle
print(windowid)

driver.find_element(By.LINK_TEXT,"nopCommerce").click()
windowsIDs = driver.window_handles

# aproach1
# parentwindowIds = windowsIDs[0]
# childwindowsid = windowsIDs[1]
# print(parentwindowIds,childwindowsid)
#
# driver.switch_to.window(childwindowsid)
# print("title of the child window", driver.title)
#
#
# driver.switch_to.window(parentwindowIds)
# print("title of the driver",driver.title)

# approach 2
# for winid in windowsIDs:
#     driver.switch_to.window(winid)
#     print(driver.title)

for windid in windowsIDs:
    driver.switch_to.window(windid)
    if driver.title == "nopCommerce demo store" or driver.title == "Free and open-source eCommerce platform. ASP.NET Core based shopping cart. - nopCommerce":
        driver.close()

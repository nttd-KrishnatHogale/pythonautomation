import time

from selenium import  webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver= webdriver.Chrome()

driver.get("https://opensource-demo.orangehrmlive.com")
driver.maximize_window()

driver.find_element(By.CSS_SELECTOR,"input[placeholder='Username']").send_keys("Admin")
driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys("admin123")
driver.find_element(By.XPATH, "//input[@placeholder='Password']").click()
time.sleep(3)

admin= driver.find_element(By.XPATH,"//*[@id='menu_admin_viewAdminModule']/b")
usermgmt = driver.find_element(By.XPATH,"//*[@id='menu_admin_UserManagement']")
users = driver.find_element(By.XPATH,"//*[@id='menu_admin_viewSystemUsers']")

act= ActionChains(driver)

act.move_to_element(admin).move_to_element(usermgmt).move_to_element(users).click().perform()

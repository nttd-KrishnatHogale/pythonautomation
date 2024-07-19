import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class DemoJsPopup():
    def demoalertclass(self):
        driver = webdriver.Chrome()
        driver.get("https://www.w3schools.com/jsref/tryit.asp?filename=tryjsref_prompt")
        driver.maximize_window()
        driver.switch_to.frame("iframeResult")
        #accept alert
        driver.find_element(By.XPATH, "//button[normalize-space()='Try it']").click()
        time.sleep(2)
        driver.switch_to.alert.accept()
        time.sleep(2)
        #accept() == yes
        #dismiss() == cancel
        #dismiss alert
        # driver.find_element(By.XPATH, "//button[normalize-space()='Try it']").click()
        # time.sleep(2)
        # driver.switch_to.alert.dismiss()
        # time.sleep(2)
        #send text in alert
        # driver.find_element(By.XPATH, "//button[normalize-space()='Try it']").click()
        # time.sleep(2)
        # driver.switch_to.alert.send_keys("RCA Academy")
        # driver.switch_to.alert.accept()
        # time.sleep(2)


DemoJsPopup().demoalertclass()

import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()

driver.get("https://www.amazon.in/?tag=msndeskstdin-21&ref=pd_sl_6oqj1kmc5n_e&adgrpid=1312818540799552&hvadid=82051422137334&hvnetw=o&hvqmt=e&hvbmt=be&hvdev=c&hvlocint=&hvlocphy=148911&hvtargid=kwd-82052090618175:loc-90&hydadcr=5626_2377281&msclkid=d900c017987d1a355d23a69c4860f5bd")
driver.back()
time.sleep(3)
driver.forward()
time.sleep(3)
driver.refresh()

time.sleep(5)

driver.close()
# driver.quit()

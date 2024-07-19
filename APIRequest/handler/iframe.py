from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# Initialize Chrome driver
driver = webdriver.Chrome()
# Open webpage with frames
driver.get("https://www.w3schools.com/html/tryit.asp?filename=tryhtml_iframe")
try:
# Switch to the frame using frame name
    WebDriverWait(driver, 1).until(EC.frame_to_be_available_and_switch_to_it((By.ID, "textareacontainer")))
# Now interact with elements inside the frame
    text_area = driver.find_element(By.XPATH, "/html/body/div[4]/div[3]/div/div/div/div[6]/div[1]/div/div/div")
    text_area.clear()
    text_area.send_keys("Hello from within the frame!")
# Optionally switch back to the default content
    driver.switch_to.default_content()
except Exception as e:
    print(f"Exception occurred: {str(e)}")
finally:
# Close the browser window
    driver.quit()
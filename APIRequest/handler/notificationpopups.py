from selenium import webdriver

ops = webdriver.ChromeOptions
ops.add_argument("--disable-notifications")
driver= webdriver.Chrome(options=ops)
driver.get("https://whatmylocation.com/#google_vignette")
driver.maximize_window()
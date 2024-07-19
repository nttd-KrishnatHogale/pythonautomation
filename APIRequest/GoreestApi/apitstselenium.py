import time
from selenium import webdriver
import requests
def perform_api_request(url, method='GET', headers=None, data=None):
    if method == 'GET':
        response = requests.get(url, headers=headers)
    elif method == 'POST':
        response = requests.post(url, headers=headers, data=data)
# Add other HTTP methods as needed (PUT, DELETE, etc.)
    else:
        raise ValueError(f"Unsupported HTTP method: {method}")
    return response

def test_api_using_selenium():
# Initialize Selenium WebDriver (e.g., Chrome)
    print("driber")
    driver = webdriver.Chrome()
    try:
# Step 1: Navigate to a page that triggers the API request (e.g., login page)
        driver.get("https://example.com/login")

# Step 2: Fill in any required login credentials if necessary (e.g., username, password)
# driver.find_element_by_name(‘username’).send_keys(‘your_username’)
# driver.find_element_by_name(‘password’).send_keys(‘your_password’)
# driver.find_element_by_name(‘login_btn’).click()

# Step 3: Wait for the API request to complete (use WebDriverWait if necessary)
# WebDriverWait(driver, 10).until(…)
# Note: The actual waiting logic depends on how the API request is triggered.

# Step 4: Get the API request URL from the Network tab in the browser’s developer tools
# api_url = ‘https://example.com/api/endpoint’

# Step 5: Make the API request using the perform_api_request function
# headers = {‘Authorization’: ‘Bearer your_access_token’} # Replace with the actual headers needed for your API
# response = perform_api_request(api_url, method=‘GET’, headers=headers)

# Step 6: Assert the response to validate the API functionality
# assert response.status_code == 200, f”API request failed with status code: {response.status_code}“
# Add more assertions based on the expected response from the API

    finally:
# Step 7: Close the browser window after the test is complete
        time.sleep(10)
        driver.quit()

test_api_using_selenium()
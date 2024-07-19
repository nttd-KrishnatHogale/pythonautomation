import pytest
from selenium import webdriver


@pytest.fixture()
def setup_and_teardown(request):
    driver = webdriver.Chrome()
    url = "https://demo.nopcommerce.com/"
    driver.get(url)
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.quit()

from login import login
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import pytest

@pytest.fixture
def setup():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_login(setup):
    driver = setup
    driver.get("https://www.saucedemo.com/")
    login(driver, "standard_user", "secret_sauce")
    
    assert "inventory.html" in driver.current_url, "Login failed"
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

def login(driver, user_name, password_name):
    wait = WebDriverWait(driver, 10)
    username = wait.until(EC.presence_of_element_located((By.NAME, "user-name")))
    username.send_keys(user_name)

    password = wait.until(EC.presence_of_element_located((By.NAME, "password")))
    password.send_keys(password_name)

    log = wait.until(EC.presence_of_element_located((By.NAME, "login-button")))
    log.send_keys(Keys.ENTER)

def test_login(setup):
    driver = setup
    driver.get("https://www.saucedemo.com/")
    login(driver, "standard_user", "secret_sauce")
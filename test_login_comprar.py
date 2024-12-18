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

def login(driver):
    wait = WebDriverWait(driver, 10)
    user = wait.until(EC.presence_of_element_located((By.NAME, "user-name")))
    user.send_keys("problem_user")

    pasword = wait.until(EC.presence_of_element_located((By.NAME, "password")))
    pasword.send_keys("secret_sauce")

    log = wait.until(EC.presence_of_element_located((By.NAME, "login-button")))
    log.click()

def select_object(driver):
    wait = WebDriverWait(driver, 10)
    name_object = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='item_4_title_link']")))
    name_object.click()

def test_login_buy(setup):
    driver = setup
    driver.get("https://www.saucedemo.com/")
    login(driver)
    select_object(driver)
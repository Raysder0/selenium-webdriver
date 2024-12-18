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

def name_object(driver):
    wait = WebDriverWait(driver, 10)
    nameObject = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='item_0_title_link']")))
    nameObject.click()

def add_car(driver):
    wait = WebDriverWait(driver, 10)
    add_to_cart = wait.until(EC.element_to_be_clickable((By.ID, "add-to-cart")))
    add_to_cart.click()

def test_login(setup):
    driver = setup
    driver.get("https://www.saucedemo.com/")

    login(driver, "standard_user", "secret_sauce")
    name_object(driver)
    add_car(driver)

from test_login import login
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

def logout(driver):
    wait = WebDriverWait(driver, 10)
    opcion = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='menu_button_container']/div/div[1]/div")))
    opcion.click()

    logout_page = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='logout_sidebar_link']")))
    logout_page.click()

def test_logout(setup):
    driver = setup
    driver.get("https://www.saucedemo.com/")

    login(driver, "visual_user", "secret_sauce")
    logout(driver)
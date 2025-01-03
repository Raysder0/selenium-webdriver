import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from automatizacion_orangeHRM.login import login
from automatizacion_orangeHRM.admin.test_admin import admin
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import pytest

@pytest.fixture
def setup():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def system_users(driver):
    wait = WebDriverWait(driver, 10)
    user_role = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[2]/div/div[2]/div/div/div[1]")))
    user_role.click()
    user_role.send_keys(Keys.ARROW_DOWN)
    user_role.send_keys(Keys.RETURN)

    wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]"))).click()

def test_system_users(setup):
    driver = setup
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    login(driver)
    admin(driver)
    system_users(driver)

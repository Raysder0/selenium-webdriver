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

def buscador(driver):
    wait = WebDriverWait(driver, 10)
    buscar = wait.until(EC.presence_of_element_located((By.NAME, "q")))
    buscar.send_keys("mir4")
    buscar.send_keys(Keys.RETURN)

def test_buscar(setup):
    driver = setup
    driver.get("https://www.google.com.pe/")
    buscador(driver)
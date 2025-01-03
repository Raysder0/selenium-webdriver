from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

def login(driver):
    wait = WebDriverWait(driver, 10)
    username = wait.until(EC.presence_of_element_located((By.NAME, "username")))
    username.send_keys("Admin")

    passw = wait.until(EC.presence_of_element_located((By.NAME, "password")))
    passw.send_keys("admin123")
    passw.send_keys(Keys.RETURN)
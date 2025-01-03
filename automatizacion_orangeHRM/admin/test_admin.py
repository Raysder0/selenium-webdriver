import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from automatizacion_orangeHRM.login import login
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def admin(driver):
    wait = WebDriverWait(driver, 10)
    
    admin = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[1]")))
    admin.click()

    

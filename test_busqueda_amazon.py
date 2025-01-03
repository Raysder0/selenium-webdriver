from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time

driver = webdriver.Chrome()

try:
    # Abre la página de Amazon
    driver.get("https://www.amazon.com")

    # Espera a que la barra de búsqueda esté visible
    search_box = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "twotabsearchtextbox"))
    )
    
    # Escribe el término de búsqueda y presiona Enter
    search_query = "laptop"
    search_box.send_keys(search_query)
    search_box.send_keys(Keys.RETURN)

    # Espera unos segundos para cargar los resultados
    time.sleep(3)

    # Extrae los nombres y precios de los primeros 5 productos
    product_names = driver.find_elements(By.XPATH, "//span[@class='a-size-medium a-color-base a-text-normal']")[:5]
    product_prices = driver.find_elements(By.XPATH, "//span[@class='a-price']")[:5]

    # Imprime los resultados
    print("Resultados de la búsqueda:")
    for i in range(min(len(product_names), len(product_prices))):
        name = product_names[i].text
        price = product_prices[i].text
        print(f"{i + 1}. {name} - {price}")

finally:
    # Cierra el navegador
    driver.quit()

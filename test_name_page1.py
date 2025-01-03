from selenium import webdriver
from selenium.webdriver.common.by import By

# Configuración del WebDriver
driver = webdriver.Chrome()  # Asegúrate de tener el controlador de Chrome instalado (chromedriver)
driver.maximize_window()  # Maximizar la ventana del navegador

try:
    # Abrir la página de Google
    driver.get("https://www.google.com")

    # Verificar el título de la página
    expected_title = "Google"
    actual_title = driver.title
    if actual_title == expected_title:
        print(f"Título verificado correctamente: {actual_title}")
    else:
        print(f"Título incorrecto. Esperado: {expected_title}, Obtenido: {actual_title}")

    # Tomar una captura de pantalla
    driver.save_screenshot("home_page.png")
    print("Captura de pantalla guardada como 'home_page.png'")

finally:
    # Cerrar el navegador
    driver.quit()

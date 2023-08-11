import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()  # Asegúrate de tener ChromeDriver instalado y en el PATH
    yield driver
    driver.quit()

def test_ver_lista_seguimiento(driver):
    url = "https://es.wikipedia.org/wiki/Wikipedia:Portada"
    driver.get(url)

    # Acceder a la página de inicio de sesión
    inicio_sesion_link = driver.find_element(By.LINK_TEXT, "Acceder")
    inicio_sesion_link.click()

    # Llenar el formulario de inicio de sesión
    nombre_usuario = driver.find_element(By.ID, "wpName1")
    nombre_usuario.send_keys("Nayid04")  # Reemplaza con tu nombre de usuario
    contrasena = driver.find_element(By.ID, "wpPassword1")
    contrasena.send_keys("tutorial2004")  # Reemplaza con tu contraseña
    inicio_sesion_button = driver.find_element(By.ID, "wpLoginAttempt")
    inicio_sesion_button.click()


    # Acceder a la lista de seguimiento
    lista_seguimiento_link = driver.find_element(By.ID, "n-help")
    lista_seguimiento_link.click()

if __name__ == "__main__":
    pytest.main(["-v", "--html=reporte.html"])

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()  # Asegúrate de tener ChromeDriver instalado y en el PATH
    yield driver
    driver.quit()

def test_buscar_articulo(driver):
    url = "https://es.wikipedia.org/wiki/Wikipedia:Portada"
    driver.get(url)

    # Realizar una búsqueda en Wikipedia (reemplaza con tu término de búsqueda)
    termino_busqueda = "Selenium"
    campo_busqueda = driver.find_element(By.ID, "searchInput")
    campo_busqueda.send_keys(termino_busqueda)
    campo_busqueda.submit()


if __name__ == "__main__":
    pytest.main(["-v", "--html=reporte.html"])

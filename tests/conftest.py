import pytest
import json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.ui import WebDriverWait

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Browser option: chrome or firefox")

@pytest.fixture(scope="class")
def setup(request):
    browser = request.config.getoption("--browser")

    if browser == "chrome":
        options = ChromeOptions()
        # Descomentar la siguiente línea para ejecutar en modo headless (sin interfaz gráfica)
        options.add_argument("--headless")
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

    
    elif browser == "firefox":
        options = FirefoxOptions()
        # Descomentar la siguiente línea para ejecutar en modo headless (sin interfaz gráfica)
        # options.add_argument("--headless")
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=options)
    
    else:
        raise ValueError("Browser option not supported: choose 'chrome' or 'firefox'.")
    
    driver.maximize_window()  # Maximiza la ventana del navegador

    request.cls.driver = driver
    request.cls.wait = WebDriverWait(driver, 10)  # Espera explícita configurada a 10 segundos
    yield driver
    driver.quit()

# Fixture para cargar credenciales
@pytest.fixture(scope="session")
def credentials():
    with open("data/credentials.json") as json_file:
        data = json.load(json_file)
    return data

# Limpieza de campos
@pytest.fixture(scope="session")
def clear_fields():
    def _clear_fields(fields):
        for field in fields:
            if field.get_attribute("value"):
                field.clear()
    return _clear_fields
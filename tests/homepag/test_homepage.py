import pytest
from selenium.webdriver.chrome.webdriver import WebDriver  # Importar el tipo específico del driver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.usefixtures("setup")
class TestHomePage:
    driver: WebDriver

    def test_validate_title_page(self):
        self.driver.get("https://demoqa.com/")
        assert self.driver.title == "DEMOQA", "El titulo de la pagina no coincide"

    def test_validate_boxes(self):
        # Valida que existan 6 cajas con los nombres correctos en la página de inicio.
        self.driver.get("https://demoqa.com/")
        # Esperar a que las cajas estén presentes en la página
        boxes = self.wait.until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".category-cards .card-body h5"))
        )
        # validar que hay 6 cajas
        assert len(boxes) == 6, f"Se encontraron {len(boxes)} cajas en lugar de 6"

        # Validar los nombres de las cajas
        expected_names = [
            "Elements", "Forms", "Alerts, Frame & Windows",
            "Widgets", "Interactions", "Book Store Application"
        ]
        actual_names = [box.text for box in boxes]
        assert actual_names == expected_names, f"Los nombres de las cajas no coinciden. Se encontró: {actual_names}"

    def test_navegation_validate_boxes(self):
        # Asegura que al hacer clic en cada una de las cajas, se redirija correctamente a la página correspondiente.
        self.driver.get("https://demoqa.com/")
        expected_urls = [
            "https://demoqa.com/elements",
            "https://demoqa.com/forms",
            "https://demoqa.com/alertsWindows",
            "https://demoqa.com/widgets",
            "https://demoqa.com/interaction",
            "https://demoqa.com/books"
        ]
    
        for index in range(len(expected_urls)):
            # Volvemos a encontrar los elementos antes de cada interacción
            box_links = self.wait.until(
                EC.presence_of_all_elements_located(
                    (By.CSS_SELECTOR, ".category-cards .card-body")
                )
            )
            box = box_links[index]
        
            box.click()
            assert self.driver.current_url == expected_urls[index], f"Redirección incorrecta para {expected_urls[index]}"
            self.driver.back()

    def test_navigation_logo_redirects_home(self):
        # Descripción: Verifica que al hacer clic en el logo se redirija de vuelta a la homepage.
        self.driver.get("https://demoqa.com/")
        # Navegar a otra sección
        elements = self.driver.find_element(By.XPATH, "//h5[contains(text(),'Forms')]")
        elements.click()
        logo = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//header/a[1]/img[1]")
            )
        )
        logo.click()
        assert self.driver.current_url == "https://demoqa.com/", "El logo no redirige correctamente a la homepage."
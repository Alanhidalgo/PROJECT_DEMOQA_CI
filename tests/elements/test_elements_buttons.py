import pytest
from selenium.webdriver.chrome.webdriver import WebDriver  # Importar el tipo específico del driver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.usefixtures("setup", "navigate_to_buttons")
class TestElementsButtons:
    driver: WebDriver

    def test_validate_buttons(self):
        # Localizadores de botones
        button_selectors = {
            "double_click": (By.ID, "doubleClickBtn"),
            "right_click": (By.ID, "rightClickBtn"),
            "click": (By.XPATH, "//button[text()='Click Me']")
        }

        # Validar que los botones se carguen y sean visibles
        for name, selector in button_selectors.items():
            button = self.wait.until(
                EC.visibility_of_element_located(selector),
                f"el boton '{name}' no esta visible en la página."
            )
            assert button.is_displayed(), f"El botón '{name}' no se muestra correctamente."
            print(f"El boton '{name}' está presente y visible.")

        # Mensaje de éxito si todos los botones están cargados
        print("Todos los botones están presentes y visibles en la página.")
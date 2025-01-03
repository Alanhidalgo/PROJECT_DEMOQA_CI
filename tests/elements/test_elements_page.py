import pytest
from selenium.webdriver.chrome.webdriver import WebDriver  # Importar el tipo específico del driver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.usefixtures("setup")
class TestElementsPage:
    driver: WebDriver
    
    def test_text_box_form(self, clear_fields, ramdom_users):
        # Seleccionamos el segundo usuario del JSON
        user = ramdom_users["users"][1]  

        # Navegar a la página de Text Box
        self.driver.get("https://demoqa.com/text-box")

        # Definir los campos del formulario y sus selectores
        form_fields = {
            "full_name": self.driver.find_element(By.ID, "userName"),
            "Email": self.driver.find_element(By.ID, "userEmail"),
            "Current_Address": self.driver.find_element(By.ID, "currentAddress"),
            "Permanent_Address": self.driver.find_element(By.ID, "permanentAddress")
        }

        # Limpiar formulario
        clear_fields(form_fields.values())

        # Llenar los campos del formulario
        form_fields["full_name"].send_keys(user["username"])
        form_fields["Email"].send_keys(user["email"])
        form_fields["Current_Address"].send_keys(user["address"])
        form_fields["Permanent_Address"].send_keys(user["city"])

        # Encontrar el botón de submit y verificar que está habilitado
        submit_button = self.driver.find_element(By.ID, "submit")
        assert submit_button.is_displayed() and submit_button.is_enabled(), "El boton de submit no esta habilitado"

        # Enviar el formulario
        submit_button.click()

        # Espera explícita para asegurar que el formulario ha sido enviado y la salida está disponible
        self.wait.until(EC.presence_of_element_located(
            (By.ID, "name")))
        self.wait.until(EC.presence_of_element_located(
            (By.ID, "email")))
        self.wait.until(EC.presence_of_element_located(
            (By.ID, "currentAddress")))
        self.wait.until(EC.presence_of_element_located(
            (By.ID, "permanentAddress")))
        
        # Diccionario para validar la salida
        output_fields = {
            "name": f"Name:{user['username']}",
            "email": f"Email:{user['email']}",
            "currentAddress": f"Current Address:{user['address']}",
            "permanentAddress": f"Permanent Address:{user['city']}"
        }


        # Validar salida
        for field_id, expect_value in output_fields.items():
            output_value = self.driver.find_element(By.ID, field_id).text
            print(f"Verificando {field_id}: esperado = '{expect_value}', actual = '{output_value}'")
            assert output_value == expect_value, f"El valor de {field_id} no coincide: {output_value}"
        
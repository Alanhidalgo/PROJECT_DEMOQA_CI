import pytest
from selenium.webdriver.chrome.webdriver import WebDriver  # Importar el tipo específico del driver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.usefixtures("setup", "navigate_to_webtables")
class TestElementsPage:
    driver: WebDriver

    def test_add_button_validation(self):
        # Encontrar el boton add y verificar que esta habilitado
        add_butoon = self.driver.find_element(By.ID, "addNewRecordButton")
        assert add_butoon.is_displayed() and add_butoon.is_enabled(), "No se encuentra el boton ADD"

    def test_form_emptys_and_enable(self, clear_fields):
        # Hacer clic en el botón 'Add'
        add_butoon = self.driver.find_element(By.ID, "addNewRecordButton")
        # Esperar hasta que el botón sea clickeable
        add_butoon.click()

        # Esperar que el formulario aparezca
        modal = self.wait.until(
            EC.visibility_of_element_located((By.CLASS_NAME, "modal-content"))
        )

        # Validar que los campos del formulario están vacíos y habilitados
        form_fields = {
            "first_name": self.driver.find_element(By.ID, "firstName"),
            "last_name": self.driver.find_element(By.ID, "lastName"),
            "email": self.driver.find_element(By.ID, "userEmail"),
            "age": self.driver.find_element(By.ID, "age"),
            "salary": self.driver.find_element(By.ID, "salary"),
            "departament": self.driver.find_element(By.ID, "department")
        }
        clear_fields(form_fields.values())

        for field_name, field_element in form_fields.items():
            assert field_element.is_enabled(), f"El campo '{field_name}' no esta habilitado"

        # validar boton submit
        submit_button = self.driver.find_element(By.ID, "submit")
        assert submit_button.is_displayed() and submit_button.is_enabled(), "El boton submit no esta disponible."

    def test_form_json_data(self, ramdom_users):
        # Seleccionamos el segundo usuario del JSON
        user = ramdom_users["users"][2]
        #capturamos el boton add
        add_butoon = self.driver.find_element(By.ID, "addNewRecordButton")
        # click boton add
        add_butoon.click()

        # Esperar que el formulario aparezca
        modal = self.wait.until(
            EC.visibility_of_element_located((By.CLASS_NAME, "modal-content"))
        )

        form_fields = {
            "first_name": self.driver.find_element(By.ID, "firstName"),
            "last_name": self.driver.find_element(By.ID, "lastName"),
            "email": self.driver.find_element(By.ID, "userEmail"),
            "age": self.driver.find_element(By.ID, "age"),
            "salary": self.driver.find_element(By.ID, "salary"),
            "departament": self.driver.find_element(By.ID, "department")
        }

        # Llenar el formulario con los datos del JSON
        form_fields["first_name"].send_keys(user["username"])
        form_fields["last_name"].send_keys(user["lastname"])
        form_fields["email"].send_keys(user["email"])
        form_fields["age"].send_keys(user["age"])
        form_fields["salary"].send_keys(user["salary"])
        form_fields["departament"].send_keys(user["state"])

        print("First name:", form_fields["first_name"].get_attribute("value"))
        print("Last name:", form_fields["last_name"].get_attribute("value"))
        print("Email:", form_fields["email"].get_attribute("value"))
        print("Age:", form_fields["age"].get_attribute("value"))
        print("Salary:", form_fields["salary"].get_attribute("value"))
        print("Department:", form_fields["departament"].get_attribute("value"))


         # validar boton submit
        submit_button = self.driver.find_element(By.ID, "submit")
        submit_button.click()

         # Esperar que el modal desaparezca
        self.wait.until(EC.invisibility_of_element_located((By.CLASS_NAME, "modal-content")))

        # Hasta aqui funciona bien el codigo

        '''# Esperar un poco para que los datos se reflejen en la tabla
        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.rt-tr-group")))   

        # Verificar si el registro ha sido añadido a la tabla
        # Obtener la última fila con XPath
        last_row = self.driver.find_element(By.XPATH, "(//div[contains(@class, 'rt-tr-group')])[last()]")
        row_data = last_row.find_elements(By.XPATH, ".//div[contains(@class, 'rt-td')]")

        # Extraer los valores de la última fila
        row_data = last_row.find_elements(By.CSS_SELECTOR, "div.rt-td")

        # Imprimir los datos de la última fila para diagnosticar
        for i, cell in enumerate(row_data):
            print(f"Celda {i}: '{cell.text}'")

        assert row_data[0].text == user["username"], "El nombre no coincide"
        assert row_data[1].text == user["lastname"], "El apellido no coincide"
        assert row_data[2].text == user["email"], "La edad no coincide"
        assert row_data[3].text == user["age"], "El correo no coincide"
        assert row_data[4].text == user["salary"], "El salario no coincide"
        assert row_data[5].text == user["state"], "El departamento no coincide" '''
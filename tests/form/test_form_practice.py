import pytest
from selenium.webdriver.chrome.webdriver import WebDriver  # Importar el tipo específico del driver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.usefixtures("setup", "navigate_to_practice_form")
class TestPracticeForm:
    driver: WebDriver

    def test_form_enable(self, clear_fields):
        # Validar que los campos del formulario están vacíos y habilitados
        form_fields = {
            "first_name": self.driver.find_element(By.ID, "firstName"),
            "last_name": self.driver.find_element(By.ID, "lastName"),
            "email": self.driver.find_element(By.ID, "userEmail"),
            "gender_male": self.driver.find_element(By.CSS_SELECTOR, "label[for='gender-radio-1']"),
            "gender_female": self.driver.find_element(By.CSS_SELECTOR, "label[for='gender-radio-2']"),
            "gender_other": self.driver.find_element(By.CSS_SELECTOR, "label[for='gender-radio-3']"),
            "mobile": self.driver.find_element(By.ID, "userNumber"),
            "date_of_birth": self.driver.find_element(By.ID, "dateOfBirthInput"),
            "subject": self.driver.find_element(By.ID, "subjectsInput"),
            "hobby_sports": self.driver.find_element(By.CSS_SELECTOR, "label[for='hobbies-checkbox-1']"),
            "hobby_reading": self.driver.find_element(By.CSS_SELECTOR, "label[for='hobbies-checkbox-2']"),
            "hobby_music": self.driver.find_element(By.CSS_SELECTOR, "label[for='hobbies-checkbox-3']"),
            "picture_upload": self.driver.find_element(By.ID, "uploadPicture"),
            "current_address": self.driver.find_element(By.ID, "currentAddress"),
            "state_city": self.driver.find_element(By.ID, "stateCity-wrapper")
        }

        #time.sleep(5)

        clear_fields(form_fields.values())

        #validamos que los campos esten habilitados
        for field_name, field_element in form_fields.items():
            assert field_element.is_enabled(), f"El campo '{field_name}' no esta habilitado"

        # validar boton submit
        submit_button = self.driver.find_element(By.ID, "submit")
        assert submit_button.is_displayed() and submit_button.is_enabled(), "El boton submit no esta disponible."

    def test_student_registration_form(self, ramdom_users):
        # Seleccionamos el usuario a enviar
        user = ramdom_users["users"][2]

        form_fields = {
            "first_name": self.driver.find_element(By.ID, "firstName"),
            "last_name": self.driver.find_element(By.ID, "lastName"),
            "email": self.driver.find_element(By.ID, "userEmail"),
            "gender_male": self.driver.find_element(By.CSS_SELECTOR, "label[for='gender-radio-1']"),
            "gender_female": self.driver.find_element(By.CSS_SELECTOR, "label[for='gender-radio-2']"),
            "gender_other": self.driver.find_element(By.CSS_SELECTOR, "label[for='gender-radio-3']"),
            "mobile": self.driver.find_element(By.ID, "userNumber"),
            "date_of_birth": self.driver.find_element(By.ID, "dateOfBirthInput"),
            "subject": self.driver.find_element(By.ID, "subjectsInput"),
            "hobby_sports": self.driver.find_element(By.CSS_SELECTOR, "label[for='hobbies-checkbox-1']"),
            "hobby_reading": self.driver.find_element(By.CSS_SELECTOR, "label[for='hobbies-checkbox-2']"),
            "hobby_music": self.driver.find_element(By.CSS_SELECTOR, "label[for='hobbies-checkbox-3']"),
            "picture_upload": self.driver.find_element(By.ID, "uploadPicture"),
            "current_address": self.driver.find_element(By.ID, "currentAddress"),
            "state_city": self.driver.find_element(By.ID, "stateCity-wrapper")
        }

        #Llenar los campos del form
        form_fields["first_name"].send_keys(user["username"])
        form_fields["last_name"].send_keys(user["lastname"])
        form_fields["email"].send_keys(user["email"])
        form_fields["gender_male"].click()
        form_fields["mobile"].send_keys(user["phone_number"])

        #boton de enviar
        submit_button = self.driver.find_element(By.ID, "submit")
        time.sleep(10)
        submit_button.click()
        time.sleep(10)
import pytest
from selenium.webdriver.chrome.webdriver import WebDriver  # Importar el tipo específico del driver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.usefixtures("setup", "navigate_to_practice_form")
class TestPracticeForm:
    driver: WebDriver

    def test_form_enable(self):
        # Validar que los campos del formulario están vacíos y habilitados
        form_fields = {
            "name": self.driver.find_element(By.ID, "firstName"),
            "lastname": self.driver.find_element(By.ID, "lastName"),
            "email": self.driver.find_element(By.ID, "userEmail"),
            "gender": 
            "mobile": self.driver.find_element(By.ID, "userNumber"),
            "date_birth": 
            "subject": self.driver.find_element(By.XPATH, "//*[@id="subjectsContainer"]/div/div[1]"),
            "hobbies": 
            "address": self.driver.find_element(By.ID, "currentAddress")   
        }
from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import uuid
from selenium.webdriver.common.action_chains import ActionChains

class StartShopPage(BasePage):
    URL = "https://demowebshop.tricentis.com/"
    generated_emails = []
    register_btn = (By.CLASS_NAME, "ico-register")
    register_title = (By.CLASS_NAME, "page-title")
    required_fields = {
        "FirstName": (By.ID, "FirstName"),
        "LastName": (By.ID, "LastName"),
        "Email": (By.ID, "Email"),
        "Password": (By.ID, "Password"),
        "ConfirmPassword": (By.ID, "ConfirmPassword"),
    }
    submit_btn = (By.ID, "register-button")
    signup_result = (By.CLASS_NAME, "result")
    login_btn = (By.CLASS_NAME, "ico-login")
    submit_login = (By.CLASS_NAME, "login-button")
    logout_btn = (By.CLASS_NAME, "ico-logout")
    computers_btn = (By.XPATH, "//a[contains(text(),'Computers')]")

    def __init__(self) -> None:
        super().__init__()
    
    def go_to_shop(self):
        self.driver.get(StartShopPage.URL)
    
    def click_on_signup(self):
        try:
            register = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable(self.register_btn)
            )
            register.click()
        
        except Exception as e:
            print(f"Error clicking on register: {str(e)}")
    
    def fill_required_input(self, input_name, signup_text):
        try:
            if input_name in self.required_fields:
                required_field = self.required_fields[input_name]
                field_element = WebDriverWait(self.driver, 10).until(
                    EC.visibility_of_element_located(required_field)
                )
                field_element.send_keys(signup_text)
                print(f"CLicked and filled on {input_name} input successfully")
            else:
                print(f"{input_name} not found")
            
        except Exception as e:
            print(f"Error filling required field: {str(e)}")
    
    def generate_email(self):
        unique_id = str(uuid.uuid4())[:8]
        generated_email = f"sa{unique_id}@test.new.com"
        self.generated_emails.append(generated_email)
        return generated_email

    def click_on_submit(self):
        try:
            confirm_register = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable(self.submit_btn)
            )
            confirm_register.click()
        
        except Exception as e:
            print(f"Error clicking on confirm register: {str(e)}")

    def clear_all_input_fields(self):
        try:
            for input_name, locator in self.required_fields.items():
                field_element = self.driver.find_element(*locator)
                field_element.clear()
                print(f"Cleared {input_name} input successfully")
        except Exception as e:
            print(f"Error clearing input fields: {str(e)}")

    def registration_result(self, result_text):
        try:
            register_success = WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located(self.signup_result)
            )
            actual_result_text = register_success.text.strip()

            if actual_result_text == result_text:
                print(f"Registration successful with message: {result_text}")
                return True
            else:
                print(f"Registration failed. Expected: {result_text}, Actual: {actual_result_text}")
                return False
            
        except Exception as e:
            print(f"Error occurred while checking registration result: {e}")
            return False

    def click_on_login(self):
        try:
            login = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable(self.login_btn)
            )
            login.click()
        
        except Exception as e:
            print(f"Error clicking on login: {str(e)}")
    
    def click_on_submit_login(self):
        try:
            confirm_login = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable(self.submit_login)
            )
            confirm_login.click()
        
        except Exception as e:
            print(f"Error clicking on confirm register: {str(e)}")

    def verify_logout_text(self, expected_text):
        try:
            # Знайдіть елемент з текстом "Logout" після логіну
            logout_element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.logout_btn)
            )

            # Отримайте текст елемента
            actual_text = logout_element.text

            # Порівняйте отриманий текст з очікуваним текстом
            assert actual_text == expected_text
            print("Logout text verified successfully.")

        except Exception as e:
            print(f"Error verifying logout text: {str(e)}")
    
    def move_to_element(self):
        computers_element = self.driver.find_element(*self.computers_btn)
        actions = ActionChains(self.driver)
        actions.move_to_element(computers_element).perform()
        sub_groups = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "sublist"))
        )

        sub_list = sub_groups.find_elements(By.TAG_NAME, "a")
        
        assert len(sub_list) == 3
        
        sub_categories = [item.text for item in sub_list]
        expected_categories = ["Desktops", "Notebooks", "Accessories"]
        assert sub_categories == expected_categories
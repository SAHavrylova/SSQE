from utils.webdriver_singleton import WebDriverSingleton
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self) -> None:
        self.driver = WebDriverSingleton().get_driver()

    def quit_driver(self):
        WebDriverSingleton._destroy_instance()

    def wait_until(self, condition, timeout=5):
        return WebDriverWait(self.driver, timeout).until(condition)

    def click_element(self, locator):
        try:
            element = self.wait_until(EC.element_to_be_clickable(locator))
            element.click()
        except Exception as e:
            print(f"An error occurred while clicking the element: {str(e)}")

    def enter_text(self, locator, text):
        input_field = self.wait_until(EC.visibility_of_element_located(locator))
        input_field.clear()
        input_field.send_keys(text)

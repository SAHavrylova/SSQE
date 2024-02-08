import allure
from allure_commons.types import AttachmentType
from utils.webdriver_singleton import WebDriverSingleton
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC



class BasePage:
    def __init__(self) -> None:
        self.driver = WebDriverSingleton().get_driver()

    def quit_driver(self):
        WebDriverSingleton._destroy_instance()

    def element_is_visible(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def element_are_visible(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator))

    def element_is_present(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def element_are_present(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator))

    def element_is_not_visible(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.invisibility_of_element_located(locator))

    def element_is_clickable(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    def go_to_element(self, element):
        self.driver.execute_script(f"arguments[0].scrollIntoView();", element)

    def wait_until(self, condition, timeout=5):
        return wait(self.driver, timeout).until(condition)

    '''def open(self):
        with allure.step(f"Open {self.PAGE_URL} page")
            self.driver.get(self.PAGE.URL)'''

    '''def is_opened(self):
        self.wait_until(EC.url_to_be(self.PAGE_URL))'''

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

    '''def make_screenshot(self, screenshot_name):
        allure.attach(
            body=self.driver.get_screenshot_as_png(),
            name=screenshot_name,
            attachment_type=AttachmentType.PNG
        )'''


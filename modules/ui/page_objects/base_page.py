import allure
from allure_commons.types import AttachmentType
from selenium.webdriver import ActionChains

from utils.webdriver_singleton import WebDriverSingleton
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self) -> None:
        self.driver = WebDriverSingleton().get_driver()
        self.driver.maximize_window()

    def quit_driver(self):
        WebDriverSingleton._destroy_instance()

    '''def __init__(self, driver) -> None:
        self.driver = driver

    def quit_driver(self):
        self.driver.quit()
    '''
    def title_is(self, locator, timeout = 5):
        return wait(self.driver, timeout).until(EC.title_is(locator))

    def element_is_visible(self, locator, timeout = 5):
        return wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def element_are_visible(self, locator, timeout = 5):
        return wait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator))

    def element_is_present(self, locator, timeout = 5):
        return wait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def element_are_present(self, locator, timeout = 5):
        return wait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator))

    def element_is_not_visible(self, locator, timeout = 5):
        return wait(self.driver, timeout).until(EC.invisibility_of_element_located(locator))

    def element_is_clickable(self, locator, timeout = 5):
        return wait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    def go_to_element(self, element):
        self.driver.execute_script(f"arguments[0].scrollIntoView();", element)

    def wait_until(self, condition, timeout = 5):
        return wait(self.driver, timeout).until(condition)

    def click_element(self, locator):
        try:
            element = self.wait_until(EC.element_to_be_clickable(locator))
            element.click()
        except Exception as e:
            print(f"An error occurred while clicking the element: {str(e)}")

    def action_move_to_element(self, element):
        action = ActionChains(self.driver)
        action.move_to_element(element)
        action.perform()

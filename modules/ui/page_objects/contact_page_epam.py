from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os


class LocatorsContactEpamPage:
    SUBMIT_CONTACT_BUTTON = (By.XPATH, "//button[@class='button-ui']")
    BUTTON = (By.CLASS_NAME, "button__content")


class ContactEpamPage(BasePage):
    URL_contact = "https://www.epam.com/about/who-we-are/contact"

    def __init__(self):
        super().__init__()
        self.locators = LocatorsContactEpamPage()

    def go_to_contact(self):
        self.driver.get(ContactEpamPage.URL_contact)

    def scroll_to_element(self, element):
        script = "arguments[0].scrollIntoView({ behavior: 'auto', block: 'center', inline: 'center' });"
        self.driver.execute_script(script, element)

    def scroll_click_submit_button(self):
        submit_btn = self.driver.find_element(*self.locators.SUBMIT_CONTACT_BUTTON)
        self.scroll_to_element(submit_btn)
        submit_btn.click()

    def validation_field(self, expected_name):
        required_label_locator = (By.XPATH, f"//label[contains(text(), '{expected_name}')]")
        required_label = self.driver.find_element(*required_label_locator)

        input_field_id = required_label.get_attribute("for")
        input_field = self.driver.find_element(By.ID, input_field_id)

        assert required_label.text.strip() == expected_name.strip()

        assert input_field.get_attribute("aria-required") == "true"

from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os


class LocatorsAboutEpamPage:
    LOGO = (By.CSS_SELECTOR, "a.header__logo-container")
    SCROLL_TO = (By.CLASS_NAME, "text-ui-23")
    TEXT_ELEMENT = (By.XPATH, "//div[contains(@class, 'text-ui-23')]//*[contains(text(), '')]")
    SPECIFIC_BUTTON = (By.CLASS_NAME, "button__content")
    BUTTON_TEXT = (By.XPATH, "//span[contains(@class, 'button__content') and text()='DOWNLOAD']")


class AboutEpamPage(BasePage):
    URL_about = "https://www.epam.com/about"

    def __init__(self) -> None:
        super().__init__()
        self.locators = LocatorsAboutEpamPage()

    def go_to_about(self):
        self.driver.get(AboutEpamPage.URL_about)

    def check_epam_title(self, exp_title):
        epam_title = self.title_is(exp_title)
        return epam_title

    def press_site_logo(self):
        self.element_is_visible(self.locators.LOGO).click()

    def scroll_to_visible_element(self, target_text):
        '''scroll_element = self.driver.find_element(*self.locators.TEXT_ELEMENT)
        if scroll_element and target_text in scroll_element.text:
            self.go_to_element(scroll_element)
        '''

        scroll = self.driver.find_elements(*self.locators.SCROLL_TO)
        scroll_element = None

        for element in scroll:
            if target_text in element.text:
                scroll_element = element
                break

        if scroll_element:
            self.driver.execute_script("arguments[0].scrollIntoView();", scroll_element)

    def click_specific_button(self, button_name):
        button = self.driver.find_elements(*self.locators.SPECIFIC_BUTTON)
        button_element = None

        for btn_element in button:
            if button_name in btn_element.text:
                button_element = btn_element
                break

        if button_element:
            button_element.click()

    def download_document(self):
        home_dir = os.path.expanduser("~")
        download_dir = os.path.join(home_dir, "Downloads")
        print("Way for:", download_dir)

        downloaded_files = os.listdir(download_dir)
        expected_file = "EPAM_Corporate_Overview_Q3_october.pdf"

        assert expected_file in downloaded_files, f"File {expected_file} not found in downloads directory"

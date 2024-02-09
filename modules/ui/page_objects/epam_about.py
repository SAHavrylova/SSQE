from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os


class LocatorsAboutEpamPage:
    LOGO = (By.CSS_SELECTOR, "a.header__logo-container")
    CURRENT_THEME_BODY = (By.CLASS_NAME, 'fonts-loaded')
    THEME_SWITCHER = (By.CSS_SELECTOR, ".theme-switcher")
    LANGUAGE_BUTTON = (By.CLASS_NAME, 'location-selector__button')
    UA_LANGUAGE = (By.XPATH, '//a[@class="location-selector__link" and @href="https://careers.epam.ua"]')
    FOOTER = (By.CSS_SELECTOR, ".footer-container")
    FOOTER_TITLE = (By.CSS_SELECTOR, '.policies .links-item')
    SCROLL_TO = (By.CLASS_NAME, "text-ui-23")
    LOCATIONS_CAROUSEL = (By.CSS_SELECTOR, '.tabs-23__item.js-tabs-item.active')
    CURRENT_OUR_LOCATION_BUTTON = (By.CLASS_NAME, "locations-viewer-23__country-btn")
    CURRENT_OUR_LOCATION_BUTTON_ACTIVE = (By.CLASS_NAME, "locations-viewer-23__country-title.list.active")
    SEARCH_BUTTON = (By.CLASS_NAME, "header-search__button")
    SEARCH_FIELD = (By.ID, 'new_form_search')
    FIND_BUTTON = (By.XPATH, "//span[@class='bth-text-layer' and contains(text(), 'Find')]")
    RESULT_COUNT = (By.CLASS_NAME, 'search-results__counter')
    SUBMIT_CONTACT_BUTTON = (By.XPATH, "//button[@class='button-ui']")
    BUTTON = (By.CLASS_NAME, "button__content")


class AboutEpamPage(BasePage):
    URL_about = "https://www.epam.com/about"

    def __init__(self) -> None:
        super().__init__()
        self.locators = LocatorsAboutEpamPage()

    def go_to_about(self):
        self.driver.get(AboutEpamPage.URL_about)

    def scroll_to_element(self, element):
        script = "arguments[0].scrollIntoView({ behavior: 'auto', block: 'center', inline: 'center' });"
        self.driver.execute_script(script, element)

    def check_epam_title(self, exp_title):
        epam_title = self.title_is(exp_title)
        return epam_title

    def press_site_logo(self):
        self.element_is_visible(self.locators.LOGO).click()

    def scrolling_to_element(self, target_text):
        self.go_to_element(self.element_is_present(target_text)

        '''scroll = self.driver.find_elements(*self.locators.SCROLL_TO)
        scroll_element = None

        for element in scroll:
            if target_text in element.text:
                scroll_element = element
                break

        if scroll_element:
            self.driver.execute_script("arguments[0].scrollIntoView();", scroll_element)
            print(f"Scrolled to {target_text} element successfully")
        else:
            print(f"{target_text} not found")
'''
    def click_on_button(self, button_name):
        button = self.driver.find_elements(*self.button_locator)
        button_element = None

        for btn_element in button:
            if button_name in btn_element.text:
                button_element = btn_element
                break

        if button_element:
            button_element.click()
            print(f"Clicked on {button_name} button successfully")
        else:
            print(f"{button_name} not found")

    def download_file(self):
        home_dir = os.path.expanduser("~")
        download_dir = os.path.join(home_dir, "Downloads")
        print("Way for:", download_dir)

        downloaded_files = os.listdir(download_dir)
        expected_file = "EPAM_Corporate_Overview_Q3_october.pdf"

        assert expected_file in downloaded_files, f"File {expected_file} not found in downloads directory"

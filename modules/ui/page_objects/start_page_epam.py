from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class StartEpamPage(BasePage):
    URL = "https://www.epam.com/"

    def __init__(self) -> None:
        super().__init__()
    
    def go_to_epam(self):
        self.driver.get(StartEpamPage.URL)
    
    def load_page(self, timeout_seconds = 3):
        wait = WebDriverWait(self.driver, timeout_seconds)
        wait.until(lambda driver: True)
    
    def check_epam_title(self, exp_title, timeout = 3):
        WebDriverWait(self.driver, timeout).until(
            EC.title_is(exp_title)
        )
        return self.driver.title == exp_title

    def get_theme(self):
        site_theme = self.driver.find_element(By.CLASS_NAME, 'fonts-loaded')
        classes = site_theme.get_attribute("class")
        return "dark-mode" if "dark-mode" in classes else "light-mode"

    def toogle_switch_elem(self):
        theme_switcher = self.driver.find_element(By.CLASS_NAME, 'switch')
        theme_switcher.click()
        
    def get_lang_location(self):
        global_language_button = self.driver.find_element(By.CLASS_NAME, 'location-selector__button')
        global_language_button.click()
        
    def change_language(self):
        ua_link_location = (By.XPATH, '//a[@class="location-selector__link" and @href="https://careers.epam.ua"]')
        ua_language = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(ua_link_location)
        )
        ua_language.click()

    def check_header_title(self, header_expected_text):
        # Locate all top-navigation__item elements
        header_items = self.driver.find_elements(By.CLASS_NAME, 'top-navigation__item')

        # Iterate over each header item
        for header_item in header_items:
            # Find the link within the header item
            header_link = header_item.find_element(By.CLASS_NAME, 'top-navigation__item-link')
            
            # Get the text of the link
            link_text = header_link.text
            
            # Check if the link text matches the expected text
            if link_text == header_expected_text:
                return True  # Return True if a match is found

        # If no match is found, print a message and return False
        return False
    
    def go_to_footer(self):
        footer_elem = self.driver.find_element(By.CLASS_NAME, "footer-container")
        self.driver.execute_script("arguments[0].scrollIntoView(true);", footer_elem)
    
    def check_footer_title(self, footer_expected_text):
        # Locate all top-navigation__item elements
        footer_items = self.driver.find_elements(By.CLASS_NAME, 'policies')

        # Iterate over each footer item
        for footer_item in footer_items:
            # Find the link within the footer item
            footer_link = footer_item.find_element(By.CLASS_NAME, 'links-item')
            
            # Get the text of the link
            link_text = footer_link.text
            
            # Check if the link text matches the expected text
            if link_text == footer_expected_text:
                return True  # Return True if a match is found

        # If no match is found, print a message and return False
        return False 
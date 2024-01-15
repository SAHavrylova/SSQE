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
        
    def change_language_to_ua(self):
        ua_link_location = (By.XPATH, '//a[@class="location-selector__link" and @href="https://careers.epam.ua"]')
        ua_language = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(ua_link_location)
        )
        ua_language.click()
    
    def language(self, choose_language):
        language_items = self.driver.find_element(By.CLASS_NAME, "location-selector__item")
        language_link = language_items.find_element(By.TAG_NAME, "a")
        language_text = language_link.text.strip()
        
        if language_text == choose_language.lower:
            WebDriverWait(self.driver, 2).until(EC.element_to_be_clickable((By.TAG_NAME, "a")))
            language_link.click()
            return True
        else:
            return False

    def check_header_title(self, header_expected_text):
        # Locate all top-navigation__item elements
        header_items = self.driver.find_elements(By.CLASS_NAME, 'top-navigation__item')

        # Iterate over each header item
        for header_item in header_items:
            # Find the link within the header item
            header_link = header_item.find_elements(By.CLASS_NAME, 'top-navigation__item-link')
            
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
        footer_items = self.driver.find_element(By.CLASS_NAME, 'policies')

        for footer_item in footer_items:
            footer_link = footer_item.find_element(By.CLASS_NAME, 'links-item')
            link_text = footer_link.text
            if link_text == footer_expected_text:
                return True  
        return False
    
    def go_to_our_locations(self):
        locations_elem = self.driver.find_element(By.CLASS_NAME, "text")
        self.driver.execute_script("arguments[0].scrollIntoView(true);", locations_elem)
    
    def check_locations_title(self):
        tabs = ["AMERICAS", "EMEA", "APAC"]

        for tab_name in tabs:
            tab_xpath = f'//a[@class="tabs-23__link" and text()="{tab_name}"]'

            try:
                tab_element = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, tab_xpath))
                )
            except:
                return False
        
        return True

    def click_location(self, choose_location):
        location_xpath = f"//a[text()='{choose_location}']"
        location_element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, location_xpath)))
        location_element.click()
        
        

        
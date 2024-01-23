from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class StartEpamPage(BasePage):
    URL = "https://www.epam.com/"
    current_theme_locator = (By.CLASS_NAME, 'fonts-loaded')
    theme_switcher_locator = (By.CSS_SELECTOR, ".theme-switcher")
    language_button_locator = (By.CLASS_NAME, 'location-selector__button')
    ua_language_locator = (By.XPATH, '//a[@class="location-selector__link" and @href="https://careers.epam.ua"]')
    footer_locator = (By.CLASS_NAME, "footer-container")
    footer_title_locator = (By.CLASS_NAME, 'policies')
    our_locations_locator = (By.CLASS_NAME, "text-ui-23")

    def __init__(self) -> None:
        super().__init__()
    
    def go_to_epam(self):
        self.driver.get(StartEpamPage.URL)
    
    def load_page(self, timeout_seconds = 3):
        wait = WebDriverWait(self.driver, timeout_seconds)
        wait.until(lambda driver: True)
    
    def wait_for_page_load(self, timeout_seconds = 10):
        WebDriverWait(self.driver, timeout_seconds).until(
            EC.presence_of_element_located((By.TAG_NAME, "body")))
    
    def check_epam_title(self, exp_title, timeout = 3):
        WebDriverWait(self.driver, timeout).until(
            EC.title_is(exp_title)
        )
        return self.driver.title == exp_title

    def get_current_theme(self):
        current_theme = self.driver.find_element(*self.current_theme_locator)
        theme = current_theme.get_attribute("class")
        return "dark-mode" if "dark-mode" in theme else "light-mode"
    
    def theme_switcher(self):
        switcher = self.driver.find_element(*self.theme_switcher_locator)
        self.driver.execute_script("arguments[0].click();", switcher)

    def get_language(self):
        global_language_button = self.driver.find_element(*self.language_button_locator)
        global_language_button.click()
        
    def change_language_to_ua(self):
        ua_language = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.ua_language_locator)
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
        
        header_items = self.driver.find_elements(By.CLASS_NAME, 'top-navigation__item') # Locate all top-navigation__item elements
        for header_item in header_items: # Iterate over each header item           
            header_link = header_item.find_element(By.CLASS_NAME, 'top-navigation__item-link') # Find the link within the header item
            link_text = header_link.text # Get the text of the link
            if link_text == header_expected_text: # Check if the link text matches the expected text
                return True  # Return True if a match is found
        
        return False # If no match is found, print a message and return False
    
    def go_to_footer(self):
        footer_elem = self.driver.find_element(*self.footer_locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", footer_elem)
    
    def check_footer_title(self, footer_expected_text):
        footer_items = self.driver.find_elements(*self.footer_title_locator)

        for footer_item in footer_items:
            footer_link = footer_item.find_element(By.CLASS_NAME, 'links-item')
            link_text = footer_link.text
            if link_text == footer_expected_text:
                return True  
        return False
    
    def scroll_to_our_locations(self):
        locations = self.driver.find_elements(*self.our_locations_locator)
        locations_element = None
        for element in locations:
            if "Locations" in element.text:
                locations_element = element
                break

        if locations_element:
            self.driver.execute_script("arguments[0].scrollIntoView();", locations_element)
        else:
            print("Our Locations not found")
    
    def check_locations_title(self):
        tabs_locations = ["AMERICAS", "EMEA", "APAC"]

        for tab_locations_name in tabs_locations:
            tab_locations_xpath = f'//a[@class="tabs-23__link" and text()="{tab_locations_name}"]'

            try:
                WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, tab_locations_xpath))
                )
            except:
                return False

        return True
    
    def click_locations(self, choose_locations_name):
        try:
            locations_titles = self.driver.find_elements(By.CLASS_NAME, "tabs-23__link")

            for title in locations_titles:
                print(f"Checking title: {title.text}")
                if title.text.strip() == choose_locations_name:
                    locations_title = title
                    break

            if locations_title:
                locations_title.click()
            else:
                print(f"Element not found: {choose_locations_name}")
        
        except Exception as e:
            print(f"Error clicking on {choose_locations_name} tab: {e}")

    def check_locations_infos(self, expected_country, expected_cities):
        try:
            locations_carousel = self.driver.find_element(By.CSS_SELECTOR, '.tabs-23__item.js-tabs-item.active')
            actual_country = locations_carousel.get_attribute('data-country')
            actual_cities = int(locations_carousel.get_attribute('data-cities'))

            assert actual_country == expected_country, f"Expected country: {expected_country}, Actual country: {actual_country}"
            assert actual_cities == expected_cities, f"Expected cities count: {expected_cities}, Actual cities count: {actual_cities}"
        
        except:
            return True
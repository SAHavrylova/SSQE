from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os


class LocatorsStartEpamPage:
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


class StartEpamPage(BasePage):
    URL = "https://www.epam.com/"

    def __init__(self):
        super().__init__()
        self.locators = LocatorsStartEpamPage()

    def go_to_epam(self):
        self.driver.get(StartEpamPage.URL)

    def scroll_to_element(self, element):
        script = "arguments[0].scrollIntoView({ behavior: 'auto', block: 'center', inline: 'center' });"
        self.driver.execute_script(script, element)

    def check_epam_title(self, exp_title):
        epam_title = self.title_is(exp_title)
        return epam_title

    def get_current_theme(self):
        current_theme = self.driver.find_element(*self.locators.CURRENT_THEME_BODY)
        theme = current_theme.get_attribute("class")
        return "dark-mode" if "dark-mode" in theme else "light-mode"

    def theme_switcher(self):
        switcher = self.driver.find_element(*self.locators.THEME_SWITCHER)
        self.driver.execute_script("arguments[0].click();", switcher)

    def get_language(self):
        global_language_button = self.driver.find_element(*self.locators.LANGUAGE_BUTTON)
        global_language_button.click()

    def change_language_to_ua(self):
        ua_language = self.element_is_clickable(self.locators.UA_LANGUAGE).click()
        return ua_language

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

        header_items = self.driver.find_elements(By.CLASS_NAME, 'top-navigation__item')
        for header_item in header_items:  # Iterate over each header item
            header_link = header_item.find_element(By.CLASS_NAME, 'top-navigation__item-link')
            link_text = header_link.text  # Get the text of the link
            if link_text == header_expected_text:  # Check if the link text matches the expected text
                return True  # Return True if a match is found

        return False  # If no match is found, print a message and return False

    def verify_footer_policies_title(self, footer_expected_text):
        self.go_to_element(self.driver.find_element(*self.locators.FOOTER))

        policies_items = self.element_are_visible(self.locators.FOOTER_TITLE)

        policies_links = [
            policies_item.text
            for policies_item in policies_items
            ]
        if footer_expected_text in policies_links:
            return True
        else:
            return False

    def scroll_to_our_locations(self):
        locations = self.driver.find_elements(*self.locators.SCROLL_TO)
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

            locations_title = None

            for title in locations_titles:
                print(f"Checking title: {title.text}")
                if title.text.strip() == choose_locations_name:
                    locations_title = title
                    break

            if locations_title:
                locations_title.click()

                # Wait for the element to become active
                WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, f"//a[text()='{choose_locations_name}']"
                                                          f"[@class='tabs-23__link js-tabs-link active']"))
                )
                print(f"Clicked on {choose_locations_name} tab, and it is now active.")
            else:
                print(f"Element not found: {choose_locations_name}")

        except Exception as e:
            print(f"Error clicking on {choose_locations_name} tab: {e}")

    def check_locations_info(self, expected_country, expected_cities):
        try:
            country_button = self.driver.find_element(By.XPATH, f"//button[@data-country-title='{expected_country}']")
            cities_count = int(country_button.get_attribute("data-cities-count"))

            assert country_button.is_displayed(), f"Expected country '{expected_country}' not found"
            assert cities_count == expected_cities, (f"Expected cities count for '{expected_country}' "
                                                     f"is {expected_cities}, but found {cities_count}")

            print(f"Country '{expected_country}' and cities count {expected_cities} verified successfully")

        except Exception as e:
            print(f"Error checking locations info: {e}")

    def click_on_current_our_location(self, choose_current_location):
        try:
            our_location_buttons = self.driver.find_elements(*self.locators.CURRENT_OUR_LOCATION_BUTTON)

            for our_location_button in our_location_buttons:
                location_title = our_location_button.find_element(By.CLASS_NAME,
                                                                  "locations-viewer-23__country-title").text
                print(f"Checking title: {location_title}")

                if location_title.strip() == choose_current_location:
                    self.scroll_to_element(our_location_button)
                    our_location_button.click()
                    print(f"Clicked on {choose_current_location} button")
                    break

            else:
                print(f"Element not found: {choose_current_location}")

        except Exception as e:
            print(f"Error clicking on {choose_current_location} tab: {e}")

    def find_and_click_search_button(self):
        self.driver.find_element(*self.locators.SEARCH_BUTTON).click()

    def enter_text_in_search_field(self, search_text):
        self.element_is_visible(self.locators.SEARCH_FIELD).send_keys(search_text)

    def click_find_button(self):
        self.element_is_visible(self.locators.FIND_BUTTON).click()

    def get_result_count_locator(self):
        return By.CLASS_NAME, 'search-results__counter'

    def verified_search_result(self):
        result_count_element = self.element_is_visible(self.locators.RESULT_COUNT)
        result_count_text = result_count_element.text

        result_count = int(result_count_text.split()[0])
        # return result_count
        print(result_count)

    ''' def press_site_logo(self):
        try:
            logo = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable(self.locators.LOGO)
            )
            logo.click()
            print(f"Logo clicked successfully.")

        except Exception as e:
            print(f"Error clicking on logo: {str(e)}")

    def scroll_click_submit_button(self):
        try:
            submit_btn = self.driver.find_element(*self.locators.SUBMIT_CONTACT_BUTTON)
            self.scroll_to_element(submit_btn)
            submit_btn.click()

        except Exception as e:
            print(f"An error occurred: {str(e)}")

    def validation_field(self, expected_name):
        try:
            required_label_locator = (By.XPATH, f"//label[contains(text(), '{expected_name}')]")
            required_label = self.driver.find_element(*required_label_locator)

            input_field_id = required_label.get_attribute("for")
            input_field = self.driver.find_element(By.ID, input_field_id)

            assert required_label.text.strip() == expected_name.strip()

            assert input_field.get_attribute("aria-required") == "true"
            print(f"Validation passed for field '{expected_name}': Field is marked as required")

        except Exception as e:
            print(f"Validation failed for field '{expected_name}': {str(e)}")

    

    def scroll_to(self, target_text):
        scroll = self.driver.find_elements(*self.locators.SCROLL_TO)
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

    def click_on_button(self, button_name):
        button = self.driver.find_elements(*self.locators.BUTTON)
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
'''
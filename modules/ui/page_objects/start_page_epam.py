import allure

from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os


class LocatorsStartEpamPage:
    CURRENT_THEME_BODY = (By.CLASS_NAME, 'fonts-loaded')
    THEME_SWITCHER = (By.CSS_SELECTOR, ".theme-switcher")
    LANGUAGE_BUTTON = (By.CLASS_NAME, 'location-selector__button')
    UA_LANGUAGE = (By.XPATH, '//a[@class="location-selector__link" and @href="https://careers.epam.ua"]')
    SCROLL_TO = (By.CLASS_NAME, "text-ui-23")
    LOCATIONS_CAROUSEL = (By.CSS_SELECTOR, '.tabs-23__item.js-tabs-item.active')
    CURRENT_OUR_LOCATION_BUTTON = (By.CLASS_NAME, "locations-viewer-23__country-btn")
    CURRENT_OUR_LOCATION_BUTTON_ACTIVE = (By.CLASS_NAME, "locations-viewer-23__country-title.list.active")

    # footer
    FOOTER = (By.CSS_SELECTOR, ".footer-container")
    FOOTER_TITLE = (By.CSS_SELECTOR, '.policies .links-item')

    # search
    SEARCH_BUTTON = (By.CLASS_NAME, "header-search__button")
    SEARCH_FIELD = (By.ID, 'new_form_search')
    FIND_BUTTON = (By.XPATH, "//span[@class='bth-text-layer' and contains(text(), 'Find')]")

    RESULT_COUNT = (By.CLASS_NAME, 'search-results__counter')



class StartEpamPage(BasePage):
    URL = "https://www.epam.com/"

    def __init__(self):
        super().__init__()
        self.locators = LocatorsStartEpamPage()

    @allure.step("Go to EPAM website")
    def go_to_epam(self):
        self.driver.get(StartEpamPage.URL)

    @allure.step("Scroll to the specified elemen")
    def scroll_to_element(self, element):
        script = "arguments[0].scrollIntoView({ behavior: 'auto', block: 'center', inline: 'center' });"
        self.driver.execute_script(script, element)

    @allure.step("Check the EPAM title")
    def check_epam_title(self, exp_title):
        epam_title = self.title_is(exp_title)
        return epam_title

    @allure.step("Get the current theme")
    def get_current_theme(self):
        current_theme = self.driver.find_element(*self.locators.CURRENT_THEME_BODY)
        theme = current_theme.get_attribute("class")
        return "dark-mode" if "dark-mode" in theme else "light-mode"

    @allure.step("Switch the theme")
    def theme_switcher(self):
        switcher = self.driver.find_element(*self.locators.THEME_SWITCHER)
        self.driver.execute_script("arguments[0].click();", switcher)

    @allure.step("Get the current language")
    def get_language(self):
        global_language_button = self.driver.find_element(*self.locators.LANGUAGE_BUTTON)
        global_language_button.click()

    @allure.step("Change the language to Ukrainian")
    def change_language_to_ua(self):
        ua_language = self.element_is_clickable(self.locators.UA_LANGUAGE).click()
        return ua_language

    @allure.step("Check the language")
    def check_language(self, choose_language):
        language_items = self.driver.find_element(By.CLASS_NAME, "location-selector__item")
        language_link = language_items.find_element(By.TAG_NAME, "a")
        language_text = language_link.text.strip()

        if language_text == choose_language.lower:
            WebDriverWait(self.driver, 2).until(EC.element_to_be_clickable((By.TAG_NAME, "a")))
            language_link.click()
            return True
        else:
            return False

    @allure.step("Check the header title")
    def check_header_title(self, header_expected_text):

        header_items = self.driver.find_elements(By.CLASS_NAME, 'top-navigation__item')
        for header_item in header_items:  # Iterate over each header item
            header_link = header_item.find_element(By.CLASS_NAME, 'top-navigation__item-link')
            link_text = header_link.text  # Get the text of the link
            if link_text == header_expected_text:  # Check if the link text matches the expected text
                return True  # Return True if a match is found

        return False  # If no match is found, print a message and return False

    @allure.step("Verify the footer policies title")
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

    @allure.step("Scroll to our locations section")
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

    @allure.step("Check the locations title")
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

    @allure.step("Click on the locations")
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

    @allure.step("Check the locations information")
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

    @allure.step("Click on the current our location")
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

    @allure.step("Find and click the search button")
    def find_and_click_search_button(self):
        self.driver.find_element(*self.locators.SEARCH_BUTTON).click()

    @allure.step("Enter text in the search field")
    def enter_text_in_search_field(self, search_text):
        self.element_is_visible(self.locators.SEARCH_FIELD).send_keys(search_text)

    @allure.step("Click the find button")
    def click_find_button(self):
        self.element_is_visible(self.locators.FIND_BUTTON).click()

    @allure.step("Verify the search result")
    def verified_search_result(self):
        result_count_element = self.element_is_visible(self.locators.RESULT_COUNT)
        result_count_text = result_count_element.text

        result_count = int(result_count_text.split()[0])
        return result_count

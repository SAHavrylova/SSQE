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
    
    def check_epam_title(self, exp_title):
        return self.driver.title == exp_title

    def get_theme(self):
        header_element = self.driver.find_element(By.CLASS_NAME, 'fonts-loaded')
        classes = header_element.get_attribute("class")
        return "dark-mode" if "dark-mode" in classes else "light-mode"

    def toogle_switch_elem(self):
        switch = self.driver.find_element(By.CLASS_NAME, "switcher")
        
    def get_location(self):
        global_language_button = self.driver.find_element(By.CLASS_NAME, 'location-selector__button')
        global_language_button.click()

    def check_location_title(self, location_language_title):
        return self.driver.title == location_language_title
        
        #find UA element on dropdown menu
    def change_language(self):
        ua_link_location = (By.XPATH, '//a[@class="location-selector__link" and @href="https://careers.epam.ua"]')
        ua_language = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(ua_link_location)
        )
        ua_language.click()
    






from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By

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
        location = self.driver.find_element(By.CLASS_NAME, "location-selector")
        location.click()

    def check_location_title(self, location_language_title):
        return self.driver.title == location_language_title
        
        #find UA element on dropdown menu
    def change_language(self, language):
        dropdown_location = self.driver.find_element(By.CLASS_NAME, "location-selector__link")
        language = dropdown_location.get_attribute("href")
        language.click()




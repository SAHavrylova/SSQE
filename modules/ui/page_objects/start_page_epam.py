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

    def get_switch_elem(self):
        switch_element = self.driver.find_element(By.CLASS_NAME, 'theme-switcher')
        return switch_element

from utils.webdriver_singleton import WebDriverSingleton

class BasePage:
    def __init__(self) -> None:
        self.driver = WebDriverSingleton().get_driver()
    
    def quit_driver(self):
        WebDriverSingleton._destroy_instance()

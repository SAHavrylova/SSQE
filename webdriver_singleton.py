from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

class WebDriverSingleton:
    _instance = None

    def __new__(cls, browser = "chrome"):
        if cls._instance is None:
            cls._instance = super(WebDriverSingleton, cls).__new__(cls)
            if browser.lower() == "chrome":
                cls._instance.driver = cls._init_chrome_driver()
            elif browser.lover() == "firefox":
                cls._instance.driver = cls._init_firefox_driver()
            else:
                raise ValueError(f"Unsupported browser: {browser}")
        
        return cls._instance
    
    @staticmethod
    def _init_chrome_driver():
        return webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    
    @staticmethod
    def _init_firefox_driver():
        gecko_driver_path = GeckoDriverManager().install()
        return webdriver.Firefox(service=FirefoxService(gecko_driver_path))

    def get_driver(self):
        return self.driver

    def quit_driver(self):
        self.driver.quit()

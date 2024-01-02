'''
import pytest
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager

@pytest.fixture
def browser():
    # Отримання шляху до ГекоДрайвера
    gecko_driver_path = GeckoDriverManager().install()

    # Ініціалізація драйвера Firefox
    driver = webdriver.Firefox()
    yield driver
    # Завершення роботи драйвера
    driver.quit()

def test_open_google(browser):
    # Відкриття сторінки Google
    browser.get("https://www.google.com")

    # Опціонально можна додати деякі перевірки чи інші кроки тестування
    assert "Google" in browser.title

# Запуск тесту
if __name__ == "__main__":
    pytest.main([__file__])
'''

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from webdriver_manager.firefox import GeckoDriverManager

@pytest.fixture
def chrome_browser():
    # Ініціалізація драйвера Chrome
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    yield driver
    # Завершення роботи драйвера
    driver.quit()

@pytest.fixture
def firefox_browser():
    # Отримання шляху до ГекоДрайвера
    gecko_driver_path = GeckoDriverManager().install()
    # Ініціалізація драйвера Firefox
    driver = webdriver.Firefox()
    yield driver
    # Завершення роботи драйвера
    driver.quit()

def test_open_google(chrome_browser, firefox_browser):
    # Відкриття сторінки Google у браузері Chrome
    chrome_browser.get("https://www.google.com")
    assert "Google" in chrome_browser.title

    # Відкриття сторінки Google у браузері Firefox
    firefox_browser.get("https://www.google.com")
    assert "Google" in firefox_browser.title


import json
import random

import pytest

from modules.api.clients.petstore_user import Petstore
from modules.ui.page_objects.contact_page_epam import ContactEpamPage
from modules.ui.page_objects.demowebshop import StartShopPage
from modules.ui.page_objects.epam_about import AboutEpamPage
from modules.ui.page_objects.saucedemo import StartSaucedemo
from modules.ui.page_objects.start_page_epam import StartEpamPage
from utils.webdriver_singleton import WebDriverSingleton


'''@pytest.fixture(scope = "module")
def driver():
    driver = WebDriverSingleton()
    driver.maximize_window()
    yield driver.get_driver()
    attach = driver.get_screenshot_as_png()
    allure.attach(attach, name = f"Screenshot {datetime.today()}", attachment_type = allure.attachment_type.PNG)
    driver.quit_driver()
'''


@pytest.fixture(scope = "function")
def start_demoshop_instance():
    shop_page = StartShopPage()
    shop_page.go_to_shop()

    yield shop_page

    shop_page.quit_driver()


@pytest.fixture(scope = "function")
def start_page_epam_instance():
    start_page = StartEpamPage()
    start_page.go_to_epam()

    yield start_page

    start_page.quit_driver()


@pytest.fixture(scope = "function")
def about_page_epam_instance():
    about_page = AboutEpamPage()
    about_page.go_to_about()

    yield about_page

    about_page.quit_driver()


@pytest.fixture(scope = "function")
def contact_page_epam_instance():
    contact_page = ContactEpamPage()
    contact_page.go_to_contact_page()

    yield contact_page

    contact_page.quit_driver()


@pytest.fixture(scope = "function")
def start_sauce_instance():
    sauce_page = StartSaucedemo()
    sauce_page.go_to_saucedemo()

    yield sauce_page

    sauce_page.quit_driver()


@pytest.fixture
def sauce_signin(start_sauce_instance):
    with open('tests/ui/sauce_username.txt', "r") as file:
        sauce_usernames = file.readlines()
    random_username = random.choice(sauce_usernames).strip()
    start_sauce_instance.enter_username(random_username)
    start_sauce_instance.enter_password()
    start_sauce_instance.click_on_login_button()
    return start_sauce_instance


@pytest.fixture(scope = "session")
def sauce_user_creds():
    with open("sauce_creds.json", "r") as file:
        data = json.load(file)
        return data["users"]


@pytest.fixture
def sauce_login(request, sauce_user_creds):
    user_index = request.param
    user = sauce_user_creds[user_index]
    return user


@pytest.fixture
def base_user_url():
    return "https://petstore.swagger.io/v2"


@pytest.fixture
def petstore(base_user_url):
    return Petstore(base_user_url)

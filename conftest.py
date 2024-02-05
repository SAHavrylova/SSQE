import pytest
import json
import requests
import random
from modules.api.clients.petstore_user import Petstore
from modules.ui.page_objects.start_page_epam import StartEpamPage
from modules.ui.page_objects.demowebshop import StartShopPage
from modules.ui.page_objects.saucedemo import StartSaucedemo


@pytest.fixture(scope="module")
def start_page_epam_instance():
    start_page = StartEpamPage()
    start_page.go_to_epam()
    
    yield start_page

    start_page.quit_driver()

@pytest.fixture(scope="module")
def start_demoshop_instance():
    shop_page = StartShopPage()
    shop_page.go_to_shop()

    yield shop_page

    shop_page.quit_driver()

@pytest.fixture(scope="module")
def start_sauce_instance():
    sauce_page = StartSaucedemo()
    sauce_page.go_to_saucedemo()

    yield sauce_page

    sauce_page.quit_driver()

@pytest.fixture
def sauce_signin(start_sauce_instance):
    with open("sauce_username.txt", "r") as file:
        sauce_usernames = file.readlines()
    random_username = random.choice(sauce_usernames).strip()
    start_sauce_instance.click_on_username_field(random_username)
    start_sauce_instance.click_on_password_field()
    start_sauce_instance.click_on_login_button()
    return start_sauce_instance

@pytest.fixture(scope="session")
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

    
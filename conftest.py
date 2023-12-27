import pytest
from modules.api.clients.swagger import Swagger

@pytest.fixture
def base_user_url():
    return "https://petstore.swagger.io/#/user"

@pytest.fixture
def valid_user_credentials():
    return {
        "username": "Svitlana", 
        "password": "Havrylova"
        }
    
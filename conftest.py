import pytest
from modules.api.clients.petstore import Petstore


@pytest.fixture
def base_user_url():
    return "https://petstore.swagger.io/v2"

@pytest.fixture
def petstore(base_user_url):
    return Petstore(base_user_url)
    
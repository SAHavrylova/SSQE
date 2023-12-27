import pytest
from modules.api.clients.swagger import Swagger

@pytest.mark.api
def test_successful_user_login(base_user_url, valid_user_credentials):
    response = requests.get(f"{base_user_url}/login")


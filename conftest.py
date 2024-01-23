import pytest
from modules.api.clients.petstore import Petstore
from modules.ui.page_objects.start_page_epam import StartEpamPage


@pytest.fixture(scope="module")
def start_page_epam_instance():
    # Setup code: create the StartEpamPage instance and navigate to the page
    start_page = StartEpamPage()
    start_page.go_to_epam()
    
    yield start_page

    start_page.quit_driver()

@pytest.fixture
def base_user_url():
    return "https://petstore.swagger.io/v2"

@pytest.fixture
def petstore(base_user_url):
    return Petstore(base_user_url)

    
from modules.ui.page_objects.sign_in_page_epam import SignInEpamPage
import pytest

@pytest.mark.epamui
def test_check_the_title_is_correct():
    # Create object page
    sign_in_epam_page = SignInEpamPage()

    #Open page epam.com
    sign_in_epam_page.go_to_epam()

    #Compare the title
    assert sign_in_epam_page.check_epam_title("EPAM | Software Engineering & Product Development Services")

    #Close the browser
    sign_in_epam_page.close()

@pytest.mark.epamui
def
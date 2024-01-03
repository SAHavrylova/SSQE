from modules.ui.page_objects.start_page_epam import StartEpamPage
import pytest

@pytest.mark.epamui
def test_check_the_title_is_correct():
    # Create object page
    start_page_epam = StartEpamPage()

    #Open page epam.com
    start_page_epam.go_to_epam()

    #Compare the title
    assert start_page_epam.check_epam_title("EPAM | Software Engineering & Product Development Services")

    #Close the browser
    start_page_epam.close()
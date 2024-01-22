from modules.ui.page_objects.start_page_epam import StartEpamPage
import pytest
import time

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

@pytest.mark.epamui
def test_the_ability_to_switch_theme():
    # Create object page
    start_page_epam = StartEpamPage()

    #Open page epam.com
    start_page_epam.go_to_epam()
    initial_theme = start_page_epam.get_current_theme()
    start_page_epam.theme_switcher()
    switched_theme = start_page_epam.get_current_theme()
    assert initial_theme != switched_theme, "Theme did not switch successfully"
    
    # Close the browser
    start_page_epam.quit_driver()


@pytest.mark.epamui
def test_that_allow_to_change_lang_to_ua():
    # Create object page
    start_page_epam = StartEpamPage()

    #Open page epam.com
    start_page_epam.go_to_epam()

    #Find location and open
    start_page_epam.get_language()

    start_page_epam.change_language_to_ua()

    assert start_page_epam.check_epam_title("EPAM Ukraine - найбільша ІТ-компанія в Україні | Вакансії", timeout = 5)
    
    start_page_epam.check_header_title("ВАКАНСІЇ")
    start_page_epam.check_header_title("НАВЧАННЯ")
    start_page_epam.check_header_title("БЛОГ")
    start_page_epam.check_header_title("ПОДІЇ")
    start_page_epam.check_header_title("ПРО КОМПАНІЮ")
    
    start_page_epam.quit_driver()

@pytest.mark.epamui
def test_check_the_policies_list():
    # Create object page
    start_page_epam = StartEpamPage()

    #Open page epam.com
    start_page_epam.go_to_epam()
    
    #Go to the bottom of the page
    start_page_epam.go_to_footer()

    #Check the policies list
    start_page_epam.check_footer_title("INVESTORS")
    start_page_epam.check_footer_title("OPEN SOURCE")
    start_page_epam.check_footer_title("PRIVACY POLICY")
    start_page_epam.check_footer_title("COOKIE POLICY")
    start_page_epam.check_footer_title("APPLICANT PRIVACY NOTICE")
    start_page_epam.check_footer_title("WEB ACCESSIBILITY")

    start_page_epam.quit_driver()

@pytest.mark.sa
def test_that_allow_to_switch_location_list_by_region():
    # Create object page
    start_page_epam = StartEpamPage()

    #Open page epam.com
    start_page_epam.go_to_epam()
    start_page_epam.scroll_to_our_locations()
    start_page_epam.check_locations_title()
    start_page_epam.click_locations("APAC")
    time.sleep(4)

    start_page_epam.quit_driver()
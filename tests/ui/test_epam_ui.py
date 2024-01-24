import pytest

@pytest.mark.epamui
def test_check_the_title_is_correct(start_page_epam_instance):
    #Compare the title
    assert start_page_epam_instance.check_epam_title("EPAM | Software Engineering & Product Development Services")

    #Close the browser

@pytest.mark.epamui
def test_the_ability_to_switch_theme(start_page_epam_instance):
    initial_theme = start_page_epam_instance.get_current_theme()
    start_page_epam_instance.theme_switcher()
    switched_theme = start_page_epam_instance.get_current_theme()
    assert initial_theme != switched_theme, "Theme did not switch successfully"


@pytest.mark.epamui
def test_that_allow_to_change_lang_to_ua(start_page_epam_instance):
    #Find location and open
    start_page_epam_instance.get_language()

    start_page_epam_instance.change_language_to_ua()

    assert start_page_epam_instance.check_epam_title("EPAM Ukraine - найбільша ІТ-компанія в Україні | Вакансії", timeout = 5)
    
    start_page_epam_instance.check_header_title("ВАКАНСІЇ")
    start_page_epam_instance.check_header_title("НАВЧАННЯ")
    start_page_epam_instance.check_header_title("БЛОГ")
    start_page_epam_instance.check_header_title("ПОДІЇ")
    start_page_epam_instance.check_header_title("ПРО КОМПАНІЮ")
    
@pytest.mark.epamui
def test_check_the_policies_list(start_page_epam_instance):

    #Check the policies list
    start_page_epam_instance.check_footer_title("INVESTORS")
    start_page_epam_instance.check_footer_title("OPEN SOURCE")
    start_page_epam_instance.check_footer_title("PRIVACY POLICY")
    start_page_epam_instance.check_footer_title("COOKIE POLICY")
    start_page_epam_instance.check_footer_title("APPLICANT PRIVACY NOTICE")
    start_page_epam_instance.check_footer_title("WEB ACCESSIBILITY")

@pytest.mark.epamui
def test_that_allow_to_switch_location_list_by_region(start_page_epam_instance):
    
    start_page_epam_instance.scroll_to_our_locations()
    start_page_epam_instance.check_locations_title()
    start_page_epam_instance.click_locations("APAC")
    start_page_epam_instance.click_on_current_our_location("INDIA")
    start_page_epam_instance.check_locations_infos("India", 5)

@pytest.mark.sa
def test_check_the_search_function(start_page_epam_instance):
    start_page_epam_instance.search_button()
    start_page_epam_instance.new_form_search("AI")

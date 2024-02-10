import pytest
from modules.ui.page_objects.start_page_epam import StartEpamPage
from modules.ui.page_objects.epam_about import AboutEpamPage
import time


@pytest.mark.epamui
def test_check_the_title_is_correct(start_page_epam_instance):
    # Compare the title
    assert start_page_epam_instance.check_epam_title("EPAM | Software Engineering & Product Development Services")

    # Close the browser


@pytest.mark.epamui
def test_the_ability_to_switch_theme(start_page_epam_instance):
    initial_theme = start_page_epam_instance.get_current_theme()
    start_page_epam_instance.theme_switcher()
    switched_theme = start_page_epam_instance.get_current_theme()
    assert initial_theme != switched_theme, "Theme did not switch successfully"


@pytest.mark.epamui
def test_that_allow_to_change_lang_to_ua(start_page_epam_instance):
    # Find location and open
    start_page_epam_instance.get_language()

    start_page_epam_instance.change_language_to_ua()

    assert start_page_epam_instance.check_epam_title("EPAM Ukraine - найбільша ІТ-компанія в Україні | Вакансії")

    start_page_epam_instance.check_header_title("ВАКАНСІЇ")
    start_page_epam_instance.check_header_title("НАВЧАННЯ")
    start_page_epam_instance.check_header_title("БЛОГ")
    start_page_epam_instance.check_header_title("ПОДІЇ")
    start_page_epam_instance.check_header_title("ПРО КОМПАНІЮ")


@pytest.mark.epamui
def test_check_the_policies_list(start_page_epam_instance):
    # Check the policies list
    start_page_epam_instance.verify_footer_policies_title("INVESTORS")
    start_page_epam_instance.verify_footer_policies_title("OPEN SOURCE")
    start_page_epam_instance.verify_footer_policies_title("PRIVACY POLICY")
    start_page_epam_instance.verify_footer_policies_title("COOKIE POLICY")
    start_page_epam_instance.verify_footer_policies_title("APPLICANT PRIVACY NOTICE")
    start_page_epam_instance.verify_footer_policies_title("WEB ACCESSIBILITY")


@pytest.mark.epamui
def test_that_allow_to_switch_location_list_by_region(start_page_epam_instance):
    start_page_epam_instance.scroll_to_our_locations()
    start_page_epam_instance.check_locations_title()
    start_page_epam_instance.click_locations("EMEA")
    start_page_epam_instance.click_locations("APAC")
    start_page_epam_instance.click_on_current_our_location("INDIA")
    start_page_epam_instance.check_locations_info("India", 5)


@pytest.mark.epamui
def test_check_the_search_function(start_page_epam_instance):
    start_page_epam_instance.find_and_click_search_button()
    start_page_epam_instance.enter_text_in_search_field("AI")
    start_page_epam_instance.click_find_button()
    start_page_epam_instance.verified_search_result()


@pytest.mark.epamui
def test_check_form_fields_validation(contact_page_epam_instance):
    contact_page_epam_instance.scroll_click_submit_button()
    fields_to_validate = [
        "Select the Reason for Your Inquiry*",
        "Last Name*",
        "First Name*",
        "Email*",
        "Phone*",
        "How did you hear about EPAM?*"
    ]
    for expected_name in fields_to_validate:
        contact_page_epam_instance.validation_field(expected_name)


@pytest.mark.epamui
def test_that_logo_lead_to_main(about_page_epam_instance):
    about_page_epam_instance.press_site_logo()
    assert about_page_epam_instance.check_epam_title("EPAM | Software Engineering & Product Development Services")


@pytest.mark.epamui
def test_that_allows_to_download_report(about_page_epam_instance):
    about_page_epam_instance.scroll_to_visible_element("a Glance")
    about_page_epam_instance.click_specific_button("DOWNLOAD")
    time.sleep(4)
    about_page_epam_instance.download_document()

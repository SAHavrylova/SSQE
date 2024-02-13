import allure
import pytest
from modules.ui.page_objects.start_page_epam import StartEpamPage
from modules.ui.page_objects.epam_about import AboutEpamPage
import time


@allure.suite("EPAM")
class TestEPAM:
    @allure.feature("Landing Page")
    class TestLandingPage:
        @allure.title("Verify the page title is correct")
        @pytest.mark.epamui
        def test_verify_page_title_is_correct(self, start_page_epam_instance):
            # Compare the title
            assert start_page_epam_instance.check_epam_title(
                "EPAM | Software Engineering & Product Development Services")

        @allure.title("Verify the ability to switch themes")
        @pytest.mark.epamui
        def test_verify_ability_to_switch_themes(self, start_page_epam_instance):
            initial_theme = start_page_epam_instance.get_current_theme()
            start_page_epam_instance.theme_switcher()
            switched_theme = start_page_epam_instance.get_current_theme()
            assert initial_theme != switched_theme, "Theme did not switch successfully"

        @allure.title("Verify the ability to change language to Ukrainian")
        @pytest.mark.epamui
        def test_verify_ability_to_change_language_to_ua(self, start_page_epam_instance):
            start_page_epam_instance.get_language()
            start_page_epam_instance.change_language_to_ua()

            assert start_page_epam_instance.check_epam_title(
                "EPAM Ukraine - найбільша ІТ-компанія в Україні | Вакансії")

            start_page_epam_instance.check_header_title("ВАКАНСІЇ")
            start_page_epam_instance.check_header_title("НАВЧАННЯ")
            start_page_epam_instance.check_header_title("БЛОГ")
            start_page_epam_instance.check_header_title("ПОДІЇ")
            start_page_epam_instance.check_header_title("ПРО КОМПАНІЮ")

        @allure.title("Verify the ability to switch location list by region")
        @pytest.mark.epamui
        def test_verify_ability_to_switch_location_list_by_region(self, start_page_epam_instance):
            start_page_epam_instance.scroll_to_our_locations()
            start_page_epam_instance.check_locations_title()
            start_page_epam_instance.click_locations("APAC")
            start_page_epam_instance.click_on_current_our_location("INDIA")
            start_page_epam_instance.check_locations_info("India", 5)

        @allure.title("Verify the search functionality")
        @pytest.mark.epamui
        def test_verify_search_functionality(self, start_page_epam_instance):
            start_page_epam_instance.find_and_click_search_button()
            start_page_epam_instance.enter_text_in_search_field("AI")
            start_page_epam_instance.click_find_button()
            start_page_epam_instance.verified_search_result()

    @allure.feature("Footer")
    class TestFooter:
        @allure.title("Verify the policies list")
        @pytest.mark.epamui
        def test_verify_policies_list(self, start_page_epam_instance):
            # Check the policies list
            start_page_epam_instance.verify_footer_policies_title("INVESTORS")
            start_page_epam_instance.verify_footer_policies_title("OPEN SOURCE")
            start_page_epam_instance.verify_footer_policies_title("PRIVACY POLICY")
            start_page_epam_instance.verify_footer_policies_title("COOKIE POLICY")
            start_page_epam_instance.verify_footer_policies_title("APPLICANT PRIVACY NOTICE")
            start_page_epam_instance.verify_footer_policies_title("WEB ACCESSIBILITY")

    @allure.feature("Contact Page")
    class TestContactPage:

        @allure.title("Verify form fields validation")
        @pytest.mark.epamui
        def test_verify_form_fields_validation(self, contact_page_epam_instance):
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

    @allure.feature("About Page")
    class TestAboutPage:
        @allure.title("Verify that logo leads to main page")
        @pytest.mark.epamui
        def test_verify_logo_leads_to_main_page(self, about_page_epam_instance):
            about_page_epam_instance.press_site_logo()
            assert about_page_epam_instance.check_epam_title(
                "EPAM | Software Engineering & Product Development Services")

        @allure.title("Verify the ability to download report")
        @pytest.mark.epamui
        def test_verify_ability_to_download_report(self, about_page_epam_instance):
            about_page_epam_instance.scroll_to_visible_element("a Glance")
            about_page_epam_instance.click_specific_button("DOWNLOAD")
            time.sleep(4)
            about_page_epam_instance.download_document()

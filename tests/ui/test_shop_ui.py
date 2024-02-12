import allure
import pytest
import random


@allure.suite("DemoShop")
class TestDemoShop:
    @allure.feature("User Registration")
    class TestUserRegistration:
        @allure.title("Verify user registration functionality")
        @pytest.mark.demoshop
        def test_user_registration(self, start_demoshop_instance):
            start_demoshop_instance.open_register_page()
            start_demoshop_instance.fill_required_form_field("FirstName", "SA")
            start_demoshop_instance.fill_required_form_field("LastName", "Test")
            generated_email = start_demoshop_instance.generate_email()
            start_demoshop_instance.fill_required_form_field("Email", generated_email)
            start_demoshop_instance.fill_required_form_field("Password", "SAnewTest")
            start_demoshop_instance.fill_required_form_field("ConfirmPassword", "SAnewTest")
            with open('generated_emails.txt', 'a') as file:  # "w" - rewrite "a" - append
                for email in start_demoshop_instance.generated_emails:
                    file.write(email + '\n')
            start_demoshop_instance.submit_register_form()
            start_demoshop_instance.registration_result("Your registration completed")

    @allure.feature("User Authentication")
    class TestUserAuthentication:
        @allure.title("Verify login functionality")
        @pytest.mark.demoshop
        def test_user_login(self, start_demoshop_instance):
            start_demoshop_instance.open_login_page()
            with open('generated_emails.txt', 'r') as file:
                generated_emails = file.readlines()
            random_email = random.choice(generated_emails).strip()
            start_demoshop_instance.fill_required_form_field("Email", random_email)
            start_demoshop_instance.fill_required_form_field("Password", "SAnewTest")
            start_demoshop_instance.submit_login_form()
            start_demoshop_instance.verify_logout_text("Log out")

    @allure.feature("Main Page")
    class TestSMainPage:
        @allure.title("Verify number of computer subgroups")
        @pytest.mark.demoshop
        def test_verify_number_of_computer_subgroups(self, start_demoshop_instance):
            start_demoshop_instance.verify_computers_sub_groups()

        @allure.title("Verify sorting functionality")
        @pytest.mark.demoshop
        def test_verify_sorting_functionality(self, start_demoshop_instance):
            start_demoshop_instance.open_login_page()
            with open('generated_emails.txt', 'r') as file:
                generated_emails = file.readlines()
            random_email = random.choice(generated_emails).strip()
            start_demoshop_instance.fill_required_form_field("Email", random_email)
            start_demoshop_instance.fill_required_form_field("Password", "SAnewTest")
            start_demoshop_instance.open_category_with_subgroups("Desktops")
            start_demoshop_instance.sort_by_option("Price: Low to High")
            start_demoshop_instance.assert_products_sorted_by_price()
            start_demoshop_instance.sort_by_option("Price: High to Low")
            start_demoshop_instance.assert_products_sorted_by_price()
            start_demoshop_instance.sort_by_option("Name: Z to A")
            start_demoshop_instance.assert_products_sorted_by_name()
            start_demoshop_instance.sort_by_option("Name: A to Z")
            start_demoshop_instance.assert_products_sorted_by_name()

        @allure.title("Verify changing number of items per page")
        @pytest.mark.demoshop
        def test_verify_changing_number_of_items_per_page(self, start_demoshop_instance):
            start_demoshop_instance.open_login_page()
            with open('generated_emails.txt', 'r') as file:
                generated_emails = file.readlines()
            random_email = random.choice(generated_emails).strip()
            start_demoshop_instance.fill_required_form_field("Email", random_email)
            start_demoshop_instance.fill_required_form_field("Password", "SAnewTest")
            start_demoshop_instance.open_category_with_subgroups("Desktops")
            start_demoshop_instance.sort_by_displays("4")
            start_demoshop_instance.validate_pagination_and_displayed_items()
            start_demoshop_instance.sort_by_displays("12")
            start_demoshop_instance.validate_pagination_and_displayed_items()

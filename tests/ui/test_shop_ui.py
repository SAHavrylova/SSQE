import allure
import pytest
import random


@allure.suite("DemoShop")
class TestDemoShop:
    @allure.feature("SignUP")
    class TestSignUP:
        @allure.title("Check sign up")
        @pytest.mark.demoshop
        def test_that_allows_sign_up(self, start_demoshop_instance):
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

        @pytest.mark.demoshop
        def test_that_allows_login(self, start_demoshop_instance):
            start_demoshop_instance.open_login_page()
            with open('generated_emails.txt', 'r') as file:
                generated_emails = file.readlines()
            random_email = random.choice(generated_emails).strip()
            start_demoshop_instance.fill_required_form_field("Email", random_email)
            start_demoshop_instance.fill_required_form_field("Password", "SAnewTest")
            start_demoshop_instance.submit_login_form()
            start_demoshop_instance.verify_logout_text("Log out")

        @pytest.mark.demoshop
        def test_verify_that_computers_have_3_subgroups(self, start_demoshop_instance):
            start_demoshop_instance.verify_computers_sub_groups()

        @pytest.mark.demoshop
        def test_that_allows_sorting_items(self, start_demoshop_instance):
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

        @pytest.mark.demoshop
        def test_that_allows_changing_number_on_page(self, start_demoshop_instance):
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

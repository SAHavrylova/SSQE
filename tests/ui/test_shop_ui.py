import pytest
import time
import random
from modules.ui.page_objects.demowebshop import StartShopPage


@pytest.mark.demoshop
def test_that_allows_sign_up(start_demoshop_instance):
    start_demoshop_instance.click_on_signup()
    start_demoshop_instance.fill_required_input("FirstName", "SA")
    start_demoshop_instance.fill_required_input("LastName", "Test")
    generated_email = start_demoshop_instance.generate_email()
    start_demoshop_instance.fill_required_input("Email", generated_email)
    start_demoshop_instance.fill_required_input("Password", "SAnewTest")
    start_demoshop_instance.fill_required_input("ConfirmPassword", "SAnewTest")
    with open('generated_emails.txt', 'a') as file: #"w" - rewrite "a" - eppend
        for email in start_demoshop_instance.generated_emails:
            file.write(email + '\n')
    start_demoshop_instance.click_on_submit()
    start_demoshop_instance.registration_result("Your registration completed")

@pytest.mark.demoshop
def test_that_allows_login(start_demoshop_instance):
    start_demoshop_instance.click_on_login()
    with open('generated_emails.txt', 'r') as file:
        generated_emails = file.readlines()
    random_email = random.choice(generated_emails).strip()
    start_demoshop_instance.fill_required_input("Email", random_email)
    start_demoshop_instance.fill_required_input("Password", "SAnewTest")
    start_demoshop_instance.click_on_submit_login()
    start_demoshop_instance.verify_logout_text("Log out")

@pytest.mark.demoshop
def test_verify_that_computers_have_3_subgroups(start_demoshop_instance):
    start_demoshop_instance.move_to_element()

@pytest.mark.demoshop
def test_that_allows_sorting_items(start_demoshop_instance):
    start_demoshop_instance.click_on_login()
    with open('generated_emails.txt', 'r') as file:
        generated_emails = file.readlines()
    random_email = random.choice(generated_emails).strip()
    start_demoshop_instance.fill_required_input("Email", random_email)
    start_demoshop_instance.fill_required_input("Password", "SAnewTest")
    start_demoshop_instance.click_on_categories_with_sub_groups("Desktops")
    start_demoshop_instance.sort_by_option("Price: Low to High")
    start_demoshop_instance.verify_by_title()
    start_demoshop_instance.sort_by_option("Price: High to Low")
    start_demoshop_instance.verify_by_title()
    start_demoshop_instance.sort_by_option("Name: Z to A")
    start_demoshop_instance.verify_by_title()
    start_demoshop_instance.sort_by_option("Name: A to Z")
    start_demoshop_instance.verify_by_title()

@pytest.mark.demoshop
def test_that_allows_changing_number_on_page(start_demoshop_instance):
    start_demoshop_instance.click_on_login()
    with open('generated_emails.txt', 'r') as file:
        generated_emails = file.readlines()
    random_email = random.choice(generated_emails).strip()
    start_demoshop_instance.fill_required_input("Email", random_email)
    start_demoshop_instance.fill_required_input("Password", "SAnewTest")
    start_demoshop_instance.click_on_categories_with_sub_groups("Desktops")
    start_demoshop_instance.sort_by_dispalays("4")
    start_demoshop_instance.verify_pagination_and_items()
    start_demoshop_instance.sort_by_dispalays("12")
    start_demoshop_instance.verify_pagination_and_items()

@pytest.mark.demoshop
def test_that_allows_adding_an_item_to_the_card(start_demoshop_instance):
    start_demoshop_instance.click_on_login()
    with open('generated_emails.txt', 'r') as file:
        generated_emails = file.readlines()
    random_email = random.choice(generated_emails).strip()
    start_demoshop_instance.fill_required_input("Email", random_email)
    start_demoshop_instance.fill_required_input("Password", "SAnewTest")
    start_demoshop_instance.click_menu_item("Books")


    time.sleep(5)

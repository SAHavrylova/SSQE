import pytest
import time
import random


@pytest.mark.demoshop
def test_that_allows_sign_up(start_demoshop_instance):
    start_demoshop_instance.click_on_signup()
    start_demoshop_instance.fill_required_input("FirstName", "SA")
    start_demoshop_instance.fill_required_input("LastName", "Test")
    generated_email = start_demoshop_instance.generate_email()
    start_demoshop_instance.fill_required_input("Email", generated_email)
    start_demoshop_instance.fill_required_input("Password", "SAnewTest")
    start_demoshop_instance.fill_required_input("ConfirmPassword", "SAnewTest")
    with open('generated_emails.txt', 'a') as file: #"w" - rewrit "a" - eppend
        for email in start_demoshop_instance.generated_emails:
            file.write(email + '\n')
    start_demoshop_instance.click_on_submit()
    start_demoshop_instance.registration_result("Your registration completed")

@pytest.mark.sa
def test_that_allows_login(start_demoshop_instance):
    start_demoshop_instance.click_on_login()
    with open('generated_emails.txt', 'r') as file:
        generated_emails = file.readlines()
    random_email = random.choice(generated_emails).strip()
    start_demoshop_instance.fill_required_input("Email", random_email)
    start_demoshop_instance.fill_required_input("Password", "SAnewTest")
    start_demoshop_instance.click_on_submit_login()
    start_demoshop_instance.verify_logout_text("Log out")
    
import pytest
import time


@pytest.mark.sa
def test_that_allows_sign_up(start_demoshop_instance):
    start_demoshop_instance.click_on_signup()
    start_demoshop_instance.fill_required_input("FirstName", "SA")
    start_demoshop_instance.fill_required_input("LastName", "Test")
    generated_email = start_demoshop_instance.generate_email()
    start_demoshop_instance.fill_required_input("Email", generated_email)
    start_demoshop_instance.fill_required_input("Password", "SAnewTest")
    start_demoshop_instance.fill_required_input("ConfirmPassword", "SAnewTest")
    with open('generated_emails.txt', 'a') as file:
        for email in start_demoshop_instance.generated_emails:
            file.write(email + '\n')
    start_demoshop_instance.click_on_submit()
    start_demoshop_instance.registration_result("Your registration completed")

@pytest.mark.sa
def 
    
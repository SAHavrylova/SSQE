import pytest
import time
import random

@pytest.mark.sa
def test_login(start_sauce_instance):
    with open("sauce_username.txt", "r") as file:
        sauce_usernames = file.readlines()
    random_username = random.choice(sauce_usernames).strip()
    start_sauce_instance.click_on_username_field(random_username)
    
    start_sauce_instance.click_on_password_field()
    start_sauce_instance.click_on_login_button()
    assert start_sauce_instance.verify_header_label("Swag Labs")


    time.sleep(5)

def test_check_all_list_of_products():
    
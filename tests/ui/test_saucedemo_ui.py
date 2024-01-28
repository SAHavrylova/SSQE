import pytest
import time
import random

@pytest.mark.sauce
def test_login(start_sauce_instance):
    with open("sauce_username.txt", "r") as file:
        sauce_usernames = file.readlines()
    random_username = random.choice(sauce_usernames).strip()
    start_sauce_instance.click_on_username_field(random_username)
    
    start_sauce_instance.click_on_password_field()
    start_sauce_instance.click_on_login_button()
    assert start_sauce_instance.verify_header_label("Swag Labs")

@pytest.mark.sauce
def test_check_all_list_of_products(sauce_signin):
    sauce_signin.verify_all_products()

@pytest.mark.sa
def test_open_product_page(start_sauce_instance):
    start_sauce_instance.click_on_username_field("standard_user")
    start_sauce_instance.click_on_password_field()
    start_sauce_instance.click_on_login_button()
    start_sauce_instance.click_on_specific_product()
    time.sleep(2)
    start_sauce_instance.verify_product_infos()
    start_sauce_instance.click_on_back_to()

    


    time.sleep(5)

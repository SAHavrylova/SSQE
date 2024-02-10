import time

import pytest
import random


@pytest.mark.sauce
def test_login(start_sauce_instance):
    with open("sauce_username.txt", "r") as file:
        sauce_usernames = file.readlines()
    random_username = random.choice(sauce_usernames).strip()
    start_sauce_instance.enter_username(random_username)

    start_sauce_instance.enter_password()
    start_sauce_instance.click_on_login_button()
    assert start_sauce_instance.check_saucedemo_title("Swag Labs")


@pytest.mark.sauce
def test_check_all_list_of_products(start_sauce_instance):
    start_sauce_instance.enter_username("standard_user")
    start_sauce_instance.enter_password()
    start_sauce_instance.click_on_login_button()
    start_sauce_instance.verify_all_products()


@pytest.mark.sauce
def test_open_product_page(start_sauce_instance):
    start_sauce_instance.enter_username("standard_user")
    start_sauce_instance.enter_password()
    start_sauce_instance.click_on_login_button()
    start_sauce_instance.click_on_specific_product()
    start_sauce_instance.verify_product_info_presence(), "Product info not found"

    start_sauce_instance.click_on_back_to()


@pytest.mark.sauce
def test_add_to_cart(start_sauce_instance):
    start_sauce_instance.enter_username("standard_user")
    start_sauce_instance.enter_password()
    start_sauce_instance.click_on_login_button()
    start_sauce_instance.add_to_cart("Sauce Labs Bike Light")
    start_sauce_instance.add_to_cart("Sauce Labs Fleece Jacket")
    start_sauce_instance.open_shopping_cart()
    start_sauce_instance.verify_added_items_in_cart()


@pytest.mark.sauce
def test_complete_order_process(start_sauce_instance):
    start_sauce_instance.enter_username("standard_user")
    start_sauce_instance.enter_password()
    start_sauce_instance.click_on_login_button()
    start_sauce_instance.add_to_cart("Sauce Labs Bike Light")
    start_sauce_instance.add_to_cart("Sauce Labs Fleece Jacket")
    start_sauce_instance.open_shopping_cart()
    start_sauce_instance.verify_added_items_in_cart()
    start_sauce_instance.click_on_checkout_button()
    assert start_sauce_instance.verify_checkout_information("Checkout: Your Information")
    start_sauce_instance.enter_firstname("New1")
    start_sauce_instance.enter_lastname("Last2")
    start_sauce_instance.enter_postal_code("123sa456")
    start_sauce_instance.click_on_continue_button()
    assert start_sauce_instance.verify_checkout_information("Checkout: Overview")
    start_sauce_instance.click_on_finish_button()
    assert start_sauce_instance.verify_checkout_information("Checkout: Complete!")


@pytest.mark.sauce
def test_change_sorting_by_name(start_sauce_instance):
    start_sauce_instance.enter_username("standard_user")
    start_sauce_instance.enter_password()
    start_sauce_instance.click_on_login_button()
    start_sauce_instance.sort_product_by_option("Name (Z to A)")
    start_sauce_instance.verify_sorted_order_by_name()
    start_sauce_instance.sort_product_by_option("Name (A to Z)")
    start_sauce_instance.verify_sorted_order_by_name()


@pytest.mark.sauce
def test_change_sorting_by_price(start_sauce_instance):
    start_sauce_instance.enter_username("standard_user")
    start_sauce_instance.enter_password()
    start_sauce_instance.click_on_login_button()
    start_sauce_instance.sort_product_by_option("Price (low to high)")
    start_sauce_instance.verify_sorted_order_by_price()
    start_sauce_instance.sort_product_by_option("Price (high to low)")
    start_sauce_instance.verify_sorted_order_by_price()

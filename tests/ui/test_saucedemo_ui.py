import time

import allure
import pytest
import random


@allure.suite("Saucedemo")
class TestSaucedemo:
    @allure.feature("User Authentication")
    class TestUserAuthentication:
        @allure.title("Verify login functionality")
        @pytest.mark.sauce
        def test_login(self, start_sauce_instance):
            with open("sauce_username.txt", "r") as file:
                sauce_usernames = file.readlines()
            random_username = random.choice(sauce_usernames).strip()
            start_sauce_instance.enter_username(random_username)

            start_sauce_instance.enter_password()
            start_sauce_instance.click_on_login_button()
            assert start_sauce_instance.check_saucedemo_title("Swag Labs")

    @allure.feature("Homepage")
    class TestHomepage:
        @allure.title("Verify all products are displayed on the main page")
        @pytest.mark.sauce
        def test_verify_all_products_displayed(self, start_sauce_instance):
            start_sauce_instance.enter_username("standard_user")
            start_sauce_instance.enter_password()
            start_sauce_instance.click_on_login_button()
            start_sauce_instance.verify_all_products_displayed()

        @allure.title("Verify opening product page")
        @pytest.mark.sauce
        def test_verify_open_product_page(self, start_sauce_instance):
            start_sauce_instance.enter_username("standard_user")
            start_sauce_instance.enter_password()
            start_sauce_instance.click_on_login_button()
            start_sauce_instance.click_on_specific_product()
            start_sauce_instance.verify_product_info_presence()

            start_sauce_instance.click_on_back_to_button()

        @allure.title("Verify sorting products by name")
        @pytest.mark.sauce
        def test_verify_sorting_products_by_name(self, start_sauce_instance):
            start_sauce_instance.enter_username("standard_user")
            start_sauce_instance.enter_password()
            start_sauce_instance.click_on_login_button()
            start_sauce_instance.sort_product_by_option("Name (Z to A)")
            start_sauce_instance.verify_sorted_order_by_name()
            start_sauce_instance.sort_product_by_option("Name (A to Z)")
            start_sauce_instance.verify_sorted_order_by_name()

        @allure.title("Verify sorting products by price")
        @pytest.mark.sauce
        def test_verify_sorting_products_by_price(self, start_sauce_instance):
            start_sauce_instance.enter_username("standard_user")
            start_sauce_instance.enter_password()
            start_sauce_instance.click_on_login_button()
            start_sauce_instance.sort_product_by_option("Price (low to high)")
            start_sauce_instance.verify_sorted_order_by_price()
            start_sauce_instance.sort_product_by_option("Price (high to low)")
            start_sauce_instance.verify_sorted_order_by_price()

    @allure.feature("Add to Cart and Checkout")
    class TestAddToCartAndCheckout:
        @allure.title("Verify add to cart functionality")
        @pytest.mark.sauce
        def test_verify_add_to_cart_functionality(self, start_sauce_instance):
            start_sauce_instance.enter_username("standard_user")
            start_sauce_instance.enter_password()
            start_sauce_instance.click_on_login_button()
            start_sauce_instance.add_product_to_cart("Sauce Labs Bike Light")
            start_sauce_instance.add_product_to_cart("Sauce Labs Fleece Jacket")
            start_sauce_instance.open_shopping_cart()
            start_sauce_instance.verify_added_items_in_cart()

        @allure.title("Verify complete order process")
        @pytest.mark.sauce
        def test_verify_complete_order_process(self, start_sauce_instance):
            start_sauce_instance.enter_username("standard_user")
            start_sauce_instance.enter_password()
            start_sauce_instance.click_on_login_button()
            start_sauce_instance.add_product_to_cart("Sauce Labs Bike Light")
            start_sauce_instance.add_product_to_cart("Sauce Labs Fleece Jacket")
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

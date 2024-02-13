import random
import logging
from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


class LocatorsStartSauceDemoShop:
    # login page
    USERNAME_FIELD = (By.CSS_SELECTOR, 'input[id="user-name"]')
    PASSWORD_FIELD = (By.CSS_SELECTOR, 'input[id="password"]')
    LOGIN_BUTTON = (By.CSS_SELECTOR, 'input[id="login-button"]')

    # main page
    PRODUCT_NAME = (By.XPATH, '//div[@class="inventory_item_label"]//div[@class="inventory_item_name "]')
    SPECIFIC_PRODUCT = (
        By.CSS_SELECTOR, f"div[class='inventory_item_label'] a[id='item_{random.randint(0, 5)}_title_link']")
    PRODUCT_DESCRIPTION = (By.XPATH, '//div[@class="inventory_item_description"]')
    SHOPPING_CART_ICON = (By.CSS_SELECTOR, 'div[id="shopping_cart_container"]')

    # product details_page
    INVENTORY_DETAILS_CONTAINER = (By.CSS_SELECTOR, 'div[class="inventory_details_container"]')
    INVENTORY_DETAILS_IMG = (By.CSS_SELECTOR, 'img[class="inventory_details_img"]')
    INVENTORY_DETAILS_NAME = (By.CSS_SELECTOR, 'div[class="inventory_details_name large_size"]')
    INVENTORY_DETAILS_DESCRIPTION = (By.CSS_SELECTOR, 'div[class="inventory_details_desc large_size"]')
    INVENTORY_DETAILS_PRICE = (By.CSS_SELECTOR, "div[class='inventory_details_price']")
    ADD_TO_CART_BUTTON = (By.XPATH, "//button[text()='Add to cart']")
    BACK_TO_PRODUCTS_BUTTON = (By.CSS_SELECTOR, 'button[id="back-to-products"]')

    # Shopping cart page
    CHECKOUT_BUTTON = (By.CSS_SELECTOR, 'button[id="checkout"]')
    CHECKOUT_TITLE = (By.CSS_SELECTOR, 'span[class="title"]')

    # checkout information page
    CONTINUE_CHECKOUT_BUTTON = (By.CSS_SELECTOR, 'input[id="continue"]')
    FIRST_NAME_FIELD = (By.CSS_SELECTOR, 'input[id="first-name"]')
    LAST_NAME_FIELD = (By.CSS_SELECTOR, 'input[id="last-name"]')
    POSTAL_CODE = (By.CSS_SELECTOR, 'input[id="postal-code"]')

    # checkout overview
    FINISH_ORDER_BUTTON = (By.CSS_SELECTOR, 'button[id="finish"]')

    # sorting option
    SORTING_BUTTON = (By.CSS_SELECTOR, 'span[class="select_container"]')
    SORT_OPTIONS_DROPDOWN = (By.CSS_SELECTOR, 'select[class="product_sort_container"]')
    INVENTORY_LIST = (By.CSS_SELECTOR, 'div[class="inventory_list"]')
    INVENTORY_ITEM = (By.CSS_SELECTOR, 'div[class="inventory_item"]')
    INVENTORY_NAME = (By.CSS_SELECTOR, 'div[class="inventory_item_name "]')
    INVENTORY_ITEM_PRICE = (By.CSS_SELECTOR, 'div[class="inventory_item_price"]')


class StartSaucedemo(BasePage):
    URL = "https://www.saucedemo.com/"
    added_items = []

    def __init__(self) -> None:
        super().__init__()
        self.locators = LocatorsStartSauceDemoShop()

    def go_to_saucedemo(self):
        self.driver.get(StartSaucedemo.URL)

    def enter_username(self, username):
        self.element_is_visible(self.locators.USERNAME_FIELD).send_keys(username)

    def enter_password(self):
        self.element_is_visible(self.locators.PASSWORD_FIELD).send_keys("secret_sauce")

    def click_on_login_button(self):
        self.element_is_visible(self.locators.LOGIN_BUTTON).click()

    def check_saucedemo_title(self, exp_title):
        saucedemo_title = self.title_is(exp_title)
        return saucedemo_title

    def verify_all_products(self):
        all_products = [
            "Sauce Labs Backpack",
            "Sauce Labs Bike Light",
            "Sauce Labs Bolt T-Shirt",
            "Sauce Labs Fleece Jacket",
            "Sauce Labs Onesie",
            "Test.allTheThings() T-Shirt (Red)"
        ]

        for products_name in all_products:
            product_name_xpath = f'//a[@id="title_link"]/div[@class="inventory_item_name" and text()="{products_name}"]'

            try:
                WebDriverWait(self.driver, 5).until(
                    EC.presence_of_element_located((By.XPATH, product_name_xpath))
                )
            except:
                return False

        return True

    def click_on_specific_product(self):
        self.click_element(self.locators.SPECIFIC_PRODUCT)

    def verify_product_info_presence(self):
        self.driver.find_elements(*self.locators.INVENTORY_DETAILS_CONTAINER)
        self.driver.find_elements(*self.locators.INVENTORY_DETAILS_IMG)
        self.driver.find_elements(*self.locators.INVENTORY_DETAILS_NAME)
        self.driver.find_elements(*self.locators.INVENTORY_DETAILS_DESCRIPTION)
        self.driver.find_elements(*self.locators.INVENTORY_DETAILS_PRICE)
        self.driver.find_elements(*self.locators.ADD_TO_CART_BUTTON)

    def click_on_back_to(self):
        try:
            self.click_element(self.locators.BACK_TO_PRODUCTS_BUTTON)
        except Exception as e:
            print(f"An error occurred while clicking on 'Back to products': {str(e)}")

    def add_to_cart(self, item_name):
        try:
            inventory_items = self.element_are_present(self.locators.PRODUCT_DESCRIPTION)

            for item in inventory_items:
                name_element = item.find_element(By.CLASS_NAME, 'inventory_item_name')
                add_button = item.find_element(By.CLASS_NAME, 'btn_inventory')
                if name_element.text.strip() == item_name:
                    add_button.click()
                    StartSaucedemo.added_items.append(item_name)
                    break

        except Exception as e:
            print(f"An error occurred: {str(e)}")

    @staticmethod
    def get_added_items():
        return StartSaucedemo.added_items

    def open_shopping_cart(self):
        self.element_is_visible(self.locators.SHOPPING_CART_ICON).click()

    def verify_added_items_in_cart(self):
        try:
            cart_items = self.driver.find_elements(By.CLASS_NAME, 'inventory_item_name')
            cart_item_names = [item.text for item in cart_items]

            added_items = self.get_added_items()

            for item in added_items:
                assert item in cart_item_names, f"{item} not found in the cart"

        except Exception as e:
            print(f"An error occurred while verifying items in the cart: {str(e)}")

    def click_on_checkout_button(self):
        self.element_is_visible(self.locators.CHECKOUT_BUTTON).click()

    def verify_checkout_information(self, checkout_info_text):
        checkout_title = self.element_is_visible(self.locators.CHECKOUT_TITLE).text
        return checkout_title == checkout_info_text

    def enter_firstname(self, first_name):
        self.element_is_visible(self.locators.FIRST_NAME_FIELD).send_keys(first_name)

    def enter_lastname(self, last_name):
        self.element_is_visible(self.locators.LAST_NAME_FIELD).send_keys(last_name)

    def enter_postal_code(self, postal_code):
        self.element_is_visible(self.locators.POSTAL_CODE).send_keys(postal_code)

    def click_on_continue_button(self):
        self.click_element(self.locators.CONTINUE_CHECKOUT_BUTTON)

    def click_on_finish_button(self):
        self.click_element(self.locators.FINISH_ORDER_BUTTON)

    '''def click_on_sort_button(self):
        self.click_element(*self.locators.SORTING_BUTTON)
    '''

    def sort_product_by_option(self, choose_option):
        try:
            self.click_element(self.locators.SORTING_BUTTON)

            option_list = self.element_is_clickable(self.locators.SORT_OPTIONS_DROPDOWN)
            select = Select(option_list)
            select.select_by_visible_text(choose_option)
            return True

        except Exception as e:
            logging.error("Error while sorting: %s", e)
            return False

    def verify_sorted_order_by_name(self):
        try:
            inventory_list = self.element_is_present(self.locators.INVENTORY_LIST)
            inventory_items = inventory_list.find_elements(*self.locators.INVENTORY_ITEM)

            for item in inventory_items:
                name_element = item.find_element(*self.locators.PRODUCT_NAME)
                name = name_element.text
                return name

        except Exception as e:
            print("Error while verifying sorted order:", e)

    def verify_sorted_order_by_price(self):
        try:
            inventory_list = self.element_is_present(self.locators.INVENTORY_LIST)
            inventory_items = inventory_list.find_elements(*self.locators.INVENTORY_ITEM)

            for item in inventory_items:
                price_element = item.find_element(*self.locators.INVENTORY_ITEM_PRICE)
                price = price_element.text
                return price

        except Exception as e:
            print("Error while verifying sorted order:", e)

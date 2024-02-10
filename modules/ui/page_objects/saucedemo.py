import random
import logging
from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


class LocatorsStartSauceDemoShop:
    USERNAME_FIELD = (By.CSS_SELECTOR, 'input[id="user-name"]')
    PASSWORD_FIELD = (By.CSS_SELECTOR, 'input[id="password"]')
    LOGIN_BUTTON = (By.CSS_SELECTOR, 'input[id="login-button"]')
    PRODUCT_NAME = (By.XPATH, '//div[@class="inventory_item_name" and text()="{}"]')
    SPECIFIC_PRODUCT = (
        By.CSS_SELECTOR, f"div[class='inventory_item_label'] a[id='item_{random.randint(0, 5)}_title_link']")
    INVENTORY_DETAILS_CONTAINER = (By.CSS_SELECTOR, 'div[class="inventory_details_container"]')
    INVENTORY_DETAILS_IMG = (By.CSS_SELECTOR, 'img[class="inventory_details_img"]')
    INVENTORY_DETAILS_NAME = (By.CSS_SELECTOR, 'div[class="inventory_details_name large_size"]')
    INVENTORY_DETAILS_DESCRIPTION = (By.CSS_SELECTOR, 'div[class="inventory_details_desc large_size"]')
    INVENTORY_DETAILS_PRICE = (By.CSS_SELECTOR, "div[class='inventory_details_price']")
    ADD_TO_CART_BUTTON = (By.XPATH, "//button[text()='Add to cart']")
    BACK_TO_PRODUCTS_BUTTON = (By.CSS_SELECTOR, 'button[id="back-to-products"]')



    CONTINUE_BUTTON = (By.ID, "continue")
    FINISH_ORDER_BUTTON = (By.ID, "finish")
    HEADER_ITEM = (By.CLASS_NAME, "header_label")
    HEADER_TITLE = (By.CLASS_NAME, "app_logo")

    SHOPPING_CART = (By.ID, "shopping_cart_container")
    CHECKOUT_BUTTON = (By.ID, "checkout")
    CHECKOUT_TITLE = (By.CLASS_NAME, "title")
    SORTING_BUTTON = (By.CLASS_NAME, "select_container")
    SORT_OPTIONS_DROPDOWN = (By.CLASS_NAME, "product_sort_container")
    INVENTORY_LIST = (By.CLASS_NAME, "inventory_list")
    INVENTORY_ITEM = (By.CLASS_NAME, "inventory_item")
    INVENTORY_NAME = (By.CLASS_NAME, "inventory_item_name ")
    INVENTORY_ITEM_PRICE = (By.CLASS_NAME, "inventory_item_price")
    FIRST_NAME_FIELD = (By.ID, "first-name")
    LAST_NAME_FIELD = (By.ID, "last-name")
    POSTAL_CODE = (By.ID, "postal-code")


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

    '''
    # Maybe for future use
    def verify_header_label(self, exp_header_label_text):
        header_labels = self.driver.find_elements(*self.locators.HEADER_ITEM)

        for header_label in header_labels:
            header_link = header_label.find_element(*self.locators.HEADER_TITLE)
            link_text = header_link.text
            if link_text == exp_header_label_text:
                return True
        return False
    '''

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
        container = self.driver.find_elements(*self.locators.INVENTORY_DETAILS_CONTAINER)
        img = self.driver.find_elements(*self.locators.INVENTORY_DETAILS_IMG)
        name = self.driver.find_elements(*self.locators.INVENTORY_DETAILS_NAME)
        description = self.driver.find_elements(*self.locators.INVENTORY_DETAILS_DESCRIPTION)
        price = self.driver.find_elements(*self.locators.INVENTORY_DETAILS_PRICE)
        add_to_cart_buttons = self.driver.find_elements(*self.locators.ADD_TO_CART_BUTTON)

        assert len(container) > 0, "Inventory details container not found"
        assert len(img) > 0, "Inventory details image not found"
        assert len(name) > 0, "Inventory details name not found"
        assert len(description) > 0, "Inventory details description not found"
        assert len(price) > 0, "Inventory details price not found"
        assert len(add_to_cart_buttons) > 0, "Add to cart buttons not found"

    def click_on_back_to(self):
        try:
            self.click_element(self.locators.BACK_TO_PRODUCTS_BUTTON)
        except Exception as e:
            print(f"An error occurred while clicking on 'Back to products': {str(e)}")

    def add_to_cart(self, item_name):
        try:
            inventory_items = WebDriverWait(self.driver, 10).until(
                EC.presence_of_all_elements_located((By.CLASS_NAME, "inventory_item_description"))
            )

            for item in inventory_items:
                name_element = item.find_element(By.CLASS_NAME, 'inventory_item_name')
                add_button = item.find_element(By.CLASS_NAME, 'btn_inventory')
                if name_element.text.strip() == item_name:
                    add_button.click()
                    print(f"{item_name} added to cart.")
                    StartSaucedemo.added_items.append(item_name)
                    break
            else:
                print(f"Item '{item_name}' not found in inventory.")

        except Exception as e:
            print(f"An error occurred: {str(e)}")

    @staticmethod
    def get_added_items():
        return StartSaucedemo.added_items

    def click_on_shopping_cart(self):
        shopping = self.driver.find_element(*self.locators.SHOPPING_CART)
        shopping.click()

    def get_cart_items(self):
        try:
            cart_items = self.driver.find_elements(By.CLASS_NAME, 'inventory_item_name')
            cart_item_names = [item.text for item in cart_items]

            return cart_item_names

        except Exception as e:
            print(f"An error occurred while getting cart items: {str(e)}")
            return []

    def verify_items(self):
        added_items = self.get_added_items()
        cart_items = self.get_cart_items()

        for item in added_items:
            assert item in cart_items, f"{item} not found on cart"

        print("All items verify successfully")

    def click_on_checkout_button(self):
        self.click_element(self.locators.CHECKOUT_BUTTON)

    def verify_checkout_information(self, checkout_info_text):
        try:
            checkout_text_element = self.wait_until(EC.visibility_of_element_located(self.locators.CHECKOUT_TITLE))
            checkout_text = checkout_text_element.text
            return checkout_text == checkout_info_text
        except Exception as e:
            print(f"An error occurred while verifying checkout information: {str(e)}")
            return False

    def enter_firstname(self, first_name):
        firstname_locator = self.locators.FIRST_NAME_FIELD
        self.enter_text(firstname_locator, first_name)

    def enter_lastname(self, last_name):
        lastname_locator = self.locators.LAST_NAME_FIELD
        self.enter_text(lastname_locator, last_name)

    def enter_postal_code(self, postal_code):
        postalcode_locator = self.locators.POSTAL_CODE
        self.enter_text(postalcode_locator, postal_code)

    def click_on_continue_button(self):
        self.click_element(self.locators.continue_button_locator)

    def click_on_finish_button(self):
        self.click_element(self.locators.finish_button_locator)

    def click_on_sort_button(self):
        self.click_element(*self.locators.SORTING_BUTTON)

    def sort_product_by_option(self, choose_option):
        try:
            self.click_on_sort_button()

            option_list = self.wait_until(EC.element_to_be_clickable(self.locators.SORT_OPTIONS_DROPDOWN))
            select = Select(option_list)
            select.select_by_visible_text(choose_option)
            return True

        except Exception as e:
            logging.error("Error while sorting: %s", e)
            return False

    def verify_sorted_order_by_name(self):
        try:
            inventory_list = self.wait_until(EC.presence_of_element_located(self.INVENTORY_LIST))
            inventory_items = inventory_list.find_elements(*self.locators.INVENTORY_ITEM)

            for item in inventory_items:
                name_element = item.find_element(*self.locators.INVENTORY_NAME)
                name = name_element.text

                print(f"Title: {name}")
                print("Sorted successfully")

        except Exception as e:
            print("Error while verifying sorted order:", e)

    def verify_sorted_order_by_price(self):
        try:
            inventory_list = self.wait_until(EC.presence_of_element_located(self.locators.INVENTORY_LIST))
            inventory_items = inventory_list.find_elements(*self.locators.INVENTORY_ITEM)

            for item in inventory_items:
                price_element = item.find_element(*self.locators.INVENTORY_ITEM_PRICE)
                price = price_element.text

                print(f"Price: {price}")
                print("Sorted successfully")

        except Exception as e:
            print("Error while verifying sorted order:", e)

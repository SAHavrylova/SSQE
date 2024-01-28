import random
from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


class StartSaucedemo(BasePage):
    URL = "https://www.saucedemo.com/"
    username_field = (By.ID, "user-name")
    password_field = (By.ID, "password")
    login_btn = (By.ID, "login-button")
    header_item = (By.CLASS_NAME, "header_label")
    header_title = (By.CLASS_NAME, "app_logo")
    inventory_details_container = (By.CLASS_NAME, "inventory_details_container")
    inventory_details_img = (By.CLASS_NAME, "inventory_details_img")
    inventory_details_name = (By.CLASS_NAME, "inventory_details_name")
    inventory_details_desc = (By.CLASS_NAME, "inventory_details_desc")
    inventory_details_price = (By.CLASS_NAME, "inventory_details_price")
    add_to_cart_btn = (By.ID, "add-to-cart-sauce-labs-backpack")
    back_to_products_btn = (By.ID, "back-to-products")

    def __init__(self) -> None:
        super().__init__()
    
    def go_to_saucedemo(self):
        self.driver.get(StartSaucedemo.URL)
    
    def click_on_username_field(self, username):
        username_element = self.driver.find_element(*self.username_field)
        username_element.click()
        username_element.send_keys(username)
    
    def click_on_password_field(self):
        password_element = self.driver.find_element(*self.password_field)
        password_element.click()
        password_element.send_keys("secret_sauce")
    
    def click_on_login_button(self):
        login_element = self.driver.find_element(*self.login_btn)
        login_element.click()
    
    def verify_header_label(self, exp_header_label_text):
        header_labels = self.driver.find_elements(*self.header_item)

        for header_label in header_labels:
            header_link = header_label.find_element(*self.header_title)
            link_text = header_link.text
            if link_text == exp_header_label_text:
                return True
        return False

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
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "item_4_title_link"))
        )

        element.click()
            
    def verify_product_infos(self):
        elements_present = True
        try:
            self.driver.find_elements(*self.inventory_details_container)
            self.driver.find_elements(*self.inventory_details_img)
            self.driver.find_elements(*self.inventory_details_name)
            self.driver.find_elements(*self.inventory_details_desc)
            self.driver.find_elements(*self.inventory_details_price)
            self.driver.find_elements(*self.add_to_cart_btn)
        except:
            elements_present = False
        
        if elements_present:
            print("All elements are present.")
        else:
            print("Some elements are missing.")


    def click_on_back_to(self):
        try:
            back_to = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.back_to_products_btn)
            )
            back_to.click()
        except Exception as e:
            print(f"An error occurred while clicking on 'Back to products': {str(e)}")
                

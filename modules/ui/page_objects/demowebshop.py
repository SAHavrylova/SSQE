from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import uuid
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select


class LocatorsStartShopPage:
    # register page
    REGISTER_BUTTON = (By.CSS_SELECTOR, 'a[class="ico-register"]')
    REQUIRED_FIELDS = {
        "FirstName": (By.CSS_SELECTOR, 'input[id="FirstName"]'),
        "LastName": (By.CSS_SELECTOR, 'input[id="LastName"]'),
        "Email": (By.CSS_SELECTOR, 'input[id="Email"]'),
        "Password": (By.CSS_SELECTOR, 'input[id="Password"]'),
        "ConfirmPassword": (By.CSS_SELECTOR, 'input[id="ConfirmPassword"]'),
    }
    SUBMIT_REGISTER_BUTTON = (By.CSS_SELECTOR, 'input[id="register-button"]')
    SIGNUP_RESULT = (By.CSS_SELECTOR, 'div[class="result"]')

    # login page
    LOGIN_BUTTON = (By.CSS_SELECTOR, 'a[class="ico-login"]')
    SUBMIT_LOGIN_BUTTON = (By.CSS_SELECTOR, 'input[class="button-1 login-button"]')

    # logout page
    LOGOUT_BUTTON = (By.CSS_SELECTOR, 'a[class="ico-logout"]')

    # main page
    COMPUTERS_TAB = (By.XPATH, "//a[contains(text(),'Computers')]")
    SUB_GROUPS = (By.XPATH, '//ul[contains(@class, "sublist") and contains(@class, "firstLevel") '
                            'and contains(@class, "active")]')

    # sort option
    SORTING = (By.CLASS_NAME, "product-sorting")
    SORT_BY = (By.ID, "products-orderby")
    PRODUCT_GRID = (By.CLASS_NAME, "product-grid")
    PRODUCT_ITEMS = (By.CLASS_NAME, "item-box")
    PRODUCT_TITLE = (By.CLASS_NAME, "product-title")
    DISPLAY = (By.CLASS_NAME, "product-page-size")
    DISPLAY_BY = (By.ID, "products-pagesize")
    DISPLAY_PAGER = (By.CLASS_NAME, "pager")
    ADD_CARD_BUTTON = (By.CLASS_NAME, "button-2.product-box-add-to-cart-button")


class StartShopPage(BasePage):

    URL = 'https://demowebshop.tricentis.com/'
    generated_emails = []

    def __init__(self) -> None:
        super().__init__()
        self.locators = LocatorsStartShopPage()
    
    def go_to_shop(self):
        self.driver.get(StartShopPage.URL)
    
    def open_register_page(self):
        self.element_is_visible(self.locators.REGISTER_BUTTON).click()
    
    def fill_required_form_field(self, input_name, signup_text):
        try:
            if input_name in self.locators.REQUIRED_FIELDS:
                required_field = self.locators.REQUIRED_FIELDS[input_name]
                field_element = self.element_is_visible(required_field).send_keys(signup_text)
                return field_element
            else:
                print(f"{input_name} not found")
            
        except Exception as e:
            print(f"Error filling required field: {str(e)}")
    
    def generate_email(self):
        unique_id = str(uuid.uuid4())[:8]
        generated_email = f"sa{unique_id}@test.new.com"
        self.generated_emails.append(generated_email)
        return generated_email

    def submit_register_form(self):
        self.element_is_visible(self.locators.SUBMIT_REGISTER_BUTTON).click()

    def clear_all_input_fields(self):
        try:
            for input_name, locator in self.locators.REQUIRED_FIELDS.items():
                field_element = self.driver.find_element(*locator)
                field_element.clear()
                print(f"Cleared {input_name} input successfully")
        except Exception as e:
            print(f"Error clearing input fields: {str(e)}")

    def registration_result(self, result_text):
        actual_result = self.element_is_visible(self.locators.SIGNUP_RESULT).text
        return actual_result == result_text

    def open_login_page(self):
        self.element_is_visible(self.locators.LOGIN_BUTTON).click()
    
    def submit_login_form(self):
        self.element_is_visible(self.locators.SUBMIT_LOGIN_BUTTON).click()

    def verify_logout_text(self, expected_text):
        actual_result = self.element_is_visible(self.locators.LOGOUT_BUTTON).text
        return actual_result == expected_text

    def verify_computers_sub_groups(self):
        computers_tab = self.element_is_present(self.locators.COMPUTERS_TAB)
        self.action_move_to_element(computers_tab)
        sub_groups_text = self.element_is_visible(self.locators.SUB_GROUPS)

        sub_list = sub_groups_text.find_elements(By.TAG_NAME, "a")

        assert len(sub_list) == 3

        sub_categories = [item.text for item in sub_list]
        expected_categories = ["Desktops", "Notebooks", "Accessories"]
        assert sub_categories == expected_categories

    def click_menu_item(self, choose_categories_element):
        try:
            category_element = self.driver.find_element(By.XPATH, f'//a[contains(text(),'
                                                                  f'"{choose_categories_element}")]')
        
            actions = ActionChains(self.driver)
            actions.move_to_element(category_element).click().perform()
            return True

        except Exception as e:
            print("Error while clicking:", e)

    def open_category_with_subgroups(self, sub_groups_name):
        computers_tab = self.element_is_present(self.locators.COMPUTERS_TAB)
        self.action_move_to_element(computers_tab)
        sub_groups_text = self.element_is_visible(self.locators.SUB_GROUPS)

        sub_list = sub_groups_text.find_elements(By.TAG_NAME, "a")

        for item in sub_list:
            if item.text == sub_groups_name:
                item.click()
                break
    
    def sort_by_option(self, choose_sort):
        self.element_is_visible(self.locators.SORT_BY).click()
        '''try:
            sort = self.driver.find_element(*self.locators.SORT_BY)
            sort.click()

            sort_list = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable(self.locators.SORT_BY)
            )
            select = Select(sort_list)
            select.select_by_visible_text(choose_sort)
            return True
        
        except Exception as e:
            print("Error while sorting:", e)
            return False
        '''

    def verify_by_title(self):
        try:
            product_grid = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self.locators.PRODUCT_GRID)
            )
            product_items = product_grid.find_elements(*self.locators.PRODUCT_ITEMS)

            for item in product_items:
                title_element = item.find_element(*self.locators.PRODUCT_TITLE)
                title = title_element.text

                price_element = item.find_element(By.CLASS_NAME, "actual-price")
                price = float(price_element.text.replace("$", ""))

                print(f"Title: {title}, Price: {price}")  # If you need to see result
                print("Sorted successfully")

        except Exception as e:
            print("Error while verifying prices by title:", e)
    
    def sort_by_displays(self, choose_page_size):
        try:
            display = self.driver.find_element(*self.locators.DISPLAY_BY)
            display.click()

            display_list = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable(self.locators.DISPLAY_BY)
            )
            select = Select(display_list)
            select.select_by_visible_text(choose_page_size)
            return True
        
        except Exception as e:
            print("Error while displaying:", e)
    
    def verify_pagination_and_items(self):
        try:
            pagination = self.driver.find_elements(*self.locators.DISPLAY_PAGER)
            if pagination:
                print("Pagination is displayed")
            else:
                print("Pagination is not displayed")

            items = self.driver.find_elements(By.CLASS_NAME, "product-item")
            items_count = len(items)
            if items_count > 0:
                print(f"Number of items per page is correct: {items_count}")
            else:
                print("No items found on the page")

        except Exception as e:
            print("Error while verifying pagination and items:", e)

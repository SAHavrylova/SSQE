import pytest
import json
import random

import webdriver_manager.drivers.chrome

from modules.api.clients.petstore_user import Petstore
from modules.ui.page_objects.start_page_epam import StartEpamPage
from modules.ui.page_objects.demowebshop import StartShopPage
from modules.ui.page_objects.saucedemo import StartSaucedemo
from utils.webdriver_singleton import WebDriverSingleton


'''
@pytest.fixture(scope = "function")
def driver():
    driver = WebDriverSingleton()
    driver.maximize_window()
    yield driver
    driver.quit()
'''


@pytest.fixture(scope="module")
def start_page_epam_instance():
    start_page = StartEpamPage()
    start_page.go_to_epam()

    yield start_page

    start_page.quit_driver()


@pytest.fixture(scope = "module")
def start_demoshop_instance():
    shop_page = StartShopPage()
    shop_page.go_to_shop()

    yield shop_page

    shop_page.quit_driver()


@pytest.fixture(scope = "module")
def start_sauce_instance():
    sauce_page = StartSaucedemo()
    sauce_page.go_to_saucedemo()

    yield sauce_page

    sauce_page.quit_driver()


@pytest.fixture
def sauce_signin(start_sauce_instance):
    with open("sauce_username.txt", "r") as file:
        sauce_usernames = file.readlines()
    random_username = random.choice(sauce_usernames).strip()
    start_sauce_instance.click_on_username_field(random_username)
    start_sauce_instance.click_on_password_field()
    start_sauce_instance.click_on_login_button()
    return start_sauce_instance


@pytest.fixture(scope = "session")
def sauce_user_creds():
    with open("sauce_creds.json", "r") as file:
        data = json.load(file)
        return data["users"]


@pytest.fixture
def sauce_login(request, sauce_user_creds):
    user_index = request.param
    user = sauce_user_creds[user_index]
    return user


@pytest.fixture
def base_user_url():
    return "https://petstore.swagger.io/v2"


@pytest.fixture
def petstore(base_user_url):
    return Petstore(base_user_url)


'''@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == 'setup':
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(name):
    driver.get_screenshot_as_file(name)


def pytest_html_report_title(report):
    report.title = "SSQE report"
'''

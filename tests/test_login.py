from selenium import webdriver
from data.inventory_data import InventoryData
from pages.login_pages import LoginPages
from pages.inventory_pages import InventoryPages
from data.login_data import LoginData
import pytest


@pytest.fixture
def setup():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")
    yield driver
    driver.quit()


@pytest.mark.positive
def test_login_success(setup):
    '''
    Login dengan data yang benar
    '''

    login = LoginPages(setup)
    inventory = InventoryPages(setup)

    login.clear_field()
    login.input_username(LoginData.username)
    login.input_password(LoginData.password)
    login.click_login_button()

    title = inventory.check_title()
    assert title == 'Swag Labs'


@pytest.mark.positive
@pytest.mark.parametrize('user', LoginData.other_users_list)
def test_login_other_user(setup, user):
    '''
    Login dengan menggunakan user lain
    '''

    login = LoginPages(setup)
    inventory = InventoryPages(setup)

    login.clear_field()
    login.input_username(user)
    login.input_password(LoginData.password)
    login.click_login_button()

    title = inventory.check_title()
    assert title == InventoryData.title

    url_invent = inventory.check_url_inventory()
    assert url_invent == InventoryData.url


@pytest.mark.positive
def test_login_locked(setup):
    '''
    Login dengan data blocked
    '''

    login = LoginPages(setup)

    login.clear_field()
    login.input_username(LoginData.locked_user)
    login.input_password(LoginData.password)
    login.click_login_button()

    assert login.error_username(), LoginData.el_neg_display
    assert login.error_password(), LoginData.el_neg_display
    assert login.error_box(), LoginData.el_neg_display
    assert login.error_msg(), LoginData.locked_error_msg


@pytest.mark.negative
@pytest.mark.parametrize('username,password,error_msg', LoginData.creds_neg_list)
def test_login_invalid_data(setup, username, password, error_msg):
    '''
    Login dengan credential negative
    '''

    login = LoginPages(setup)

    login.clear_field()
    login.input_username(username)
    login.input_password(password)
    login.click_login_button()

    assert login.error_username(), LoginData.el_neg_display
    assert login.error_password(), LoginData.el_neg_display
    assert login.error_box(), LoginData.el_neg_display
    assert login.error_msg() == error_msg


@pytest.mark.negative
def test_access_inventory(setup):
    '''
    Langsung akses page inventory tanpa login dulu
    '''

    inventory = InventoryPages(setup)
    login = LoginPages(setup)

    inventory.live_access_without_login()
    assert login.cek_url_login() == LoginData.url[0]
    assert login.error_username(), LoginData.el_neg_display
    assert login.error_password(), LoginData.el_neg_display
    assert login.error_box(), LoginData.el_neg_display
    assert login.error_msg() == InventoryData.forbidden_access_page

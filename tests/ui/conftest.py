from selenium import webdriver
from selene import browser
import pytest
import config
from qa_guru_diploma.data.user import User
from qa_guru_diploma.utils import attach
import data


@pytest.fixture(scope='function')
def user():
    user = User(
        full_name=data.user_name,
        email=data.user_login_email,
        phone=data.user_login_phone,
        password=data.user_password
    )
    return user


@pytest.fixture(scope='function', autouse=True)
def driver_management():
    browser.config.base_url = config.base_url
    driver_options = webdriver.ChromeOptions()
    driver_options.add_argument('--headless')
    browser.config.driver_options = driver_options
    browser.config.window_height = 1080
    browser.config.window_width = 1920

    yield

    attach.add_html(browser)
    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_video(browser)

    browser.quit()
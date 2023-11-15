import os
from qa_guru_diploma import utils
from typing import Literal
from pydantic_settings import BaseSettings
from appium.options.android import UiAutomator2Options
from appium.options.ios import XCUITestOptions
from dotenv import load_dotenv
from selenium.webdriver.chrome.options import Options
from selene import browser

BASE_DIR = os.path.dirname(__file__)


class Config(BaseSettings):
    selenoid_login: str = ''
    selenoid_password: str = ''
    browser_version: str = ''
    test_site_lang: str = 'ru'
    base_url: str = f'https://my.litefinance.vn/{test_site_lang}'
    context: Literal['local_emulator', 'local_real', 'bstack', 'web'] = 'web'
    driver_remote_url: str = ''
    bstack_userName: str = ''
    bstack_accessKey: str = ''
    timeout: float = 10.0
    android_app_url: str = ''
    ios_app_url: str = ''
    appWaitActivity: str = ''

    android_platformVersion: Literal['11.0', '12.0', '13.0', '10.0'] = '11.0'
    android_deviceName: Literal[
        'Samsung Galaxy S22 Ultra',
        'Google Pixel 7 Pro',
        'OnePlus 9',
        'Android Emulator',
        'AJJJ6R3107000937'
    ] = 'Samsung Galaxy S22 Ultra'
    android_device_uid: str = ''
    android_avd: str = ''

    ios_platformVersion: Literal['14', '15', '16'] = '14'
    ios_deviceName: Literal[
        'iPhone 14 Pro Max',
        'iPhone XS',
        'iPhone 11',
    ] = 'iPhone 14 Pro Max'

    @property
    def bstack_credentials(self):
        load_dotenv(utils.file.relative_from_root('.env.bstack_credentials'))
        self.bstack_userName = os.getenv('bstack_userName')
        self.bstack_accessKey = os.getenv('bstack_accessKey')
        return {
            'userName': self.bstack_userName,
            'accessKey': self.bstack_accessKey
        }

    def get_selenoid_link(self):
        load_dotenv(utils.file.relative_from_root('.env.selenoid_credentials'))
        self.selenoid_login = os.getenv('selenoid_login')
        self.selenoid_password = os.getenv('selenoid_password')
        return f"https://{self.selenoid_login}:{self.selenoid_password}@selenoid.autotests.cloud/wd/hub"

    def is_bstack_run(self, platform):
        if platform == 'android':
            return self.android_app_url.startswith('bs://')
        elif platform == 'ios':
            return self.ios_app_url.startswith('bs://')

    def driver_options(self, platform_name):
        if platform_name == 'android':

            options = UiAutomator2Options().load_capabilities(
                {
                    # Specify device and os_version for testing
                    "platformName": 'Android',
                    "platformVersion": self.android_platformVersion,
                    "deviceName": self.android_deviceName,
                    # Set URL of the application under test
                    "app": self.android_app_url if (
                            self.android_app_url.startswith('/') or self.is_bstack_run(platform_name))
                    else utils.file.relative_from_root(self.android_app_url),
                    'appWaitActivity': self.appWaitActivity,
                }
            )

            if self.context == 'local_emulator':
                options.set_capability('avd', self.android_avd)
            if self.context == 'local_real':
                options.set_capability('uid', self.android_device_uid)

            if self.context == 'bstack':
                options.set_capability(  # Set other BrowserStack capabilities
                    'bstack:options', {
                        "projectName": "First Python project",
                        "buildName": "browserstack-build-1",
                        "sessionName": "BStack first_test",
                        # Set your access credentials
                        **self.bstack_credentials
                    })

        elif platform_name == 'ios':
            if self.context == 'bstack':
                options = XCUITestOptions().load_capabilities(
                    {
                        # Set URL of the application under test
                        "app": self.ios_app_url if (
                                self.ios_app_url.startswith('/') or self.is_bstack_run(platform_name))
                        else utils.file.relative_from_root(self.ios_app_url),
                        # Specify device and os_version for testing
                        "deviceName": self.ios_deviceName,
                        "platformName": platform_name,
                        "platformVersion": self.ios_platformVersion,
                        # Set other BrowserStack capabilities
                        "bstack:options": {
                            **self.bstack_credentials,
                            "projectName": "First Python Local project",
                            "buildName": "browserstack-build-1",
                            "sessionName": "BStack local_test",
                            "local": "false",
                        },
                    }
                )
        elif platform_name == 'web':
            options = Options()
            selenoid_capabilities = {
                "browserName": "chrome",
                "browserVersion": self.browser_version,
                "selenoid:options": {
                    "enableVNC": True,
                    "enableVideo": True
                }
            }
            options.capabilities.update(selenoid_capabilities)

        return options

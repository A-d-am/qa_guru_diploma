from allure_commons._allure import step
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have
from tests.conftest import ios


@ios
def test_sample_ios_app():
    text_to_input = 'Hello,world!'
    with step('Click on Text button'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, "Text Button")).click()

    with step(f'Type {text_to_input}'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, "Text Input")).send_keys(
            text_to_input + "\n"
        )
    with step(f'Output result should have {text_to_input}'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, "Text Output")).should(
            have.exact_text(text_to_input)
        )
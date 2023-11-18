from selene import browser, have
import allure
from appium.webdriver.common.appiumby import AppiumBy


# noinspection PyMethodMayBeStatic
class SimpleAppMainPage:

    def click_on_text_button(self):
        with allure.step('Нажимаем на Text button'):
            browser.element((AppiumBy.ACCESSIBILITY_ID, "Text Button")).click()

    def click_on_text_input_field(self):
        with allure.step('Нажимаем на поле ввода'):
            browser.element((AppiumBy.ACCESSIBILITY_ID,"Text Input")).click()

    def type_into_text_input_field(self, value):
        with allure.step(f'Вводим в Text Input текст: {value}'):
            browser.element((AppiumBy.ACCESSIBILITY_ID, "Text Input")).send_keys(
                value + "\n"
            )

    def expected_text_is_in_output(self, value):
        with allure.step(f'На экране должен появиться текст:  {value}'):
            browser.element((AppiumBy.ACCESSIBILITY_ID, "Text Output")).should(
                have.exact_text(value)
            )

    def click_on_alert_button(self):
        with allure.step('Нажимаем на Alert'):
            browser.element((AppiumBy.ACCESSIBILITY_ID, "Alert")).click()

    def click_on_ok_button_in_alert(self):
        with allure.step('Закрываем Alert нажатием на OK'):
            browser.element((AppiumBy.ACCESSIBILITY_ID, "OK")).click()




from selene import browser, have
import allure
from appium.webdriver.common.appiumby import AppiumBy


# noinspection PyMethodMayBeStatic
class WikipediaOnboardingPage:

    def click_on_skip_button(self):
        with allure.step('Нажимаем на кнопку "Пропустить"'):
            browser.element((AppiumBy.ID, "org.wikipedia:id/fragment_onboarding_skip_button")).click()

    def click_on_continue_button(self):
        with allure.step('Нажимаем на кнопку "Продолжить"'):
            browser.element((AppiumBy.ID, 'org.wikipedia:id/fragment_onboarding_forward_button')).click()

    def verify_screen_title_text(self, onboarding_step, expected_title_text):
        with allure.step(
                f'Проверяем, что в заголовке {onboarding_step} шага онбординга есть текст {expected_title_text}'):
            assert browser.element((AppiumBy.ID, 'org.wikipedia:id/primaryTextView')).should(have.text(expected_title_text))

    def click_on_accept_send_anon_data(self):
        with allure.step('Соглашаемся с отправкой анонимной даты'):
            browser.element((AppiumBy.ID, 'org.wikipedia:id/acceptButton')).click()

    def open_onboarding_step(self, value):
        step_number = value
        with allure.step(f'Нажимаем на кнопку продолжить, пока не откроется {step_number} шаг онбординга'):
            for i in range(step_number-1):
                self.click_on_continue_button()

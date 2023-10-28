from selene import browser, be
import allure


# noinspection PyMethodMayBeStatic
class ResetPasswordPage:
    reset_password_page_link = '/reset-password'

    def type_login(self, value):
        with allure.step(f'Вводим {value} в поле логина в попапе Восстановление пароля'):
            browser.element('#resetpasswordrequestform-login').should(be.blank).type(value)

    def type_verification_code(self, value):
        with allure.step(f'Вводим {value} в поле проверочного кода'):
            browser.element('#resetpasswordemailform-code').should(be.blank).type(value)

    def type_new_password(self, value):
        with allure.step(f'Вводим {value} в поле нового пароля'):
            browser.element('#resetpasswordemailform-password').should(be.blank).type(value)
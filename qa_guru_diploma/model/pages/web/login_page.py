from selene import browser, have, be
import allure
from qa_guru_diploma.data.user import User
from tests.conftest import project_config


# noinspection PyMethodMayBeStatic
class LoginPage:

    def type_login(self, value):
        with allure.step(f'Вводим {value} в поле логина'):
            browser.element('#login-popup').should(be.blank).type(value)

    def type_password(self, value):
        with allure.step(f'Вводим {value} в поле пароля'):
            browser.element('#password-popup').should(be.blank).type(value)

    def submit(self):
        with allure.step('Нажимаем на кнопку Войти'):
            browser.element('#submit_form').click()

    def go_to_registration(self):
        with allure.step('Нажимаем на гиперссылку "Регистрация"'):
            browser.element(f'[href="/{config.test_site_lang}/registration/popup"]').click()

    def open_reset_password_popup(self):
        with allure.step('Нажимаем на гиперссылку "Забыли пароль?"'):
            browser.element(f'[href="/{config.test_site_lang}/reset-password"]').click()

    def login_user(self, user: User):
        self.type_login(user.email)
        self.type_password(user.password)
        self.submit()

    def should_be_logged_in(self, value):
        with allure.step(f'Проверяем, что {value} указано в хедере, подтверждаем, что юзер осуществил вход'):
            assert browser.element('.header_main_user_box').element('.name').should(have.text(value)), \
                f'Login error: there is no {value} username in the header'

    def should_be_empty_login_field_error(self):
        field_error_message = browser.element('.field-login-popup').element('.field_error_message')
        with ((allure.step('Проверяем, что упала ошибка пустого поля логина'))):
            assert field_error_message.should(
                have.text('ПОЛЕ EMAIL ИЛИ ТЕЛЕФОН НЕОБХОДИМО ЗАПОЛНИТЬ')), "Wrong 'empty login field' error"

    def should_be_empty_password_field_error(self):
        field_error_message = browser.element('.field-password-popup').element('.field_error_message')
        with allure.step('Проверяем, что упала ошибка пустого поля пароля'):
            assert field_error_message.should(
                have.text('ПОЛЕ ПАРОЛЬ НЕОБХОДИМО ЗАПОЛНИТЬ')), 'Wrong "empty password field" error'

    def should_be_wrong_login_or_password_error(self):
        field_error_message = browser.element('.field-password-popup').element('.field_error_message')
        with allure.step('Проверяем, что упала ошибка неверного логина или пароля'):
            assert field_error_message.should(
                have.text('НЕВЕРНЫЙ ЛОГИН ИЛИ ПАРОЛЬ')), 'Wrong "invalid login or password" error'

    def should_be_opened(self):
        exp_url = '?openPopup=%2Fru%2Flogin%2Fpopup'
        with allure.step('Проверяем, что открыта страница логина'):
            assert exp_url in browser.driver.current_url, (f'Wrong url opened: '
                                                           f'expected {exp_url}, got {browser.driver.current_url}')

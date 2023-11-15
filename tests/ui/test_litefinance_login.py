from selene import browser, have
import config
from qa_guru_diploma.application import app
import allure
from allure_commons.types import Severity
from qa_guru_diploma.model.pages.reset_password_page import ResetPasswordPage
import pytest
import data
@pytest.fixture(scope='function')
def user():
    user = User(
        full_name='Surname Name',
        email='user@domain.com',
        phone='phone number',
        password='password',
        not_used_phone_number='phone number',
    )
    return user


@allure.tag("web")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "suprun")
@allure.epic("Логин пользователя")
@allure.feature("Позитивные проверки логина")
@allure.story("Юзер может залогиниться с помощью почты")
def test_success_login_with_email(user):
    app.open()
    app.header.click_on_sign_in_link()
    app.login_page.type_login(user.email)
    app.login_page.type_password(user.password)
    app.login_page.submit()
    app.login_page.should_be_logged_in(user.full_name)


@allure.tag("web")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "suprun")
@allure.epic("Логин пользователя")
@allure.feature("Позитивные проверки логина")
@allure.story("Юзер может залогиниться с помощью телефона")
def test_success_login_with_phone(user):
    app.open()
    app.header.click_on_sign_in_link()
    app.login_page.type_login(user.phone)
    app.login_page.type_password(user.password)
    app.login_page.submit()
    app.login_page.should_be_logged_in(user.full_name)


@allure.tag("web")
@allure.severity(Severity.NORMAL)
@allure.label("owner", "suprun")
@allure.epic("Логин пользователя")
@allure.feature("Ошибки")
@allure.story(
    "Падают ошибки пустых полей (логина и пароля) по нажатию на кнопку 'Войти' с пустыми полями логина и пароля ")
def test_login_popup_empty_fields_errors():
    app.open()
    app.header.click_on_sign_in_link()
    app.login_page.submit()
    app.login_page.should_be_empty_login_field_error()
    app.login_page.should_be_empty_password_field_error()


@allure.tag("web")
@allure.severity(Severity.NORMAL)
@allure.label("owner", "suprun")
@allure.epic("Логин пользователя")
@allure.feature("Ошибки")
@allure.story("Падает ошибка пустого поля логина по нажатию на кнопку 'Войти' с пустым логином")
def test_login_popup_empty_login_field_error():
    app.open()
    app.header.click_on_sign_in_link()
    app.login_page.type_password('password')
    app.login_page.submit()
    app.login_page.should_be_empty_login_field_error()


@allure.tag("web")
@allure.severity(Severity.NORMAL)
@allure.label("owner", "suprun")
@allure.epic("Логин пользователя")
@allure.feature("Ошибки")
@allure.story("Падает ошибка пустого поля логина по нажатию на кнопку 'Войти' с пустым логином")
def test_login_popup_empty_password_field_error():
    app.open()
    app.header.click_on_sign_in_link()
    app.login_page.type_login('user@domain.com')
    app.login_page.submit()
    app.login_page.should_be_empty_password_field_error()


@allure.tag("web")
@allure.severity(Severity.NORMAL)
@allure.label("owner", "suprun")
@allure.epic("Логин пользователя")
@allure.feature("Ошибки")
@allure.story("Падает ошибка 'Неверный логин или пароль' по нажатию на кнопку 'Войти' с неправильным паролем")
def test_login_popup_wrong_password_error(user):
    app.open()
    app.header.click_on_sign_in_link()
    app.login_page.type_login(user.email)
    app.login_page.type_password('NeverBeenAPassword123')
    app.login_page.submit()
    app.login_page.should_be_wrong_login_or_password_error()


@allure.tag("web")
@allure.severity(Severity.NORMAL)
@allure.label("owner", "suprun")
@allure.epic("Логин пользователя")
@allure.feature("Ошибки")
@allure.story(
    "Падает ошибка 'Неверный логин или пароль' по нажатию на кнопку 'Войти' с незарегистрированным логином (почта)")
def test_login_popup_not_registered_login_error_email(user):
    app.open()
    app.header.click_on_sign_in_link()
    app.login_page.type_login('neverbeenregisteredinlf@mail.ru')
    app.login_page.type_password('NeverBeenAPassword123')
    app.login_page.submit()
    app.login_page.should_be_wrong_login_or_password_error()


@allure.tag("web")
@allure.severity(Severity.NORMAL)
@allure.label("owner", "suprun")
@allure.epic("Логин пользователя")
@allure.feature("Ошибки")
@allure.story(
    "Падает ошибка 'Неверный логин или пароль' по нажатию на кнопку 'Войти' с незарегистрированным логином (телефон)")
@pytest.mark.skip(reason='')
def test_login_popup_not_registered_login_error_phone(user):
    app.open()
    app.header.click_on_sign_in_link()
    app.login_page.type_login(data.not_used_phone_number)
    app.login_page.type_password('NeverBeenAPassword123')
    app.login_page.submit()
    app.login_page.should_be_wrong_login_or_password_error()


@allure.tag("web")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "suprun")
@allure.epic("Логин пользователя")
@allure.feature("Позитивные проверки логина")
@allure.story("Юзер может перейти в попап регистрации из логина")
def test_open_registration_tab_from_login_popup():
    app.open()
    app.header.click_on_sign_in_link()
    app.login_page.go_to_registration()

    exp_url = f'{config.base_url}?openPopup=%2Fru%2Fregistration%2Fpopup'

    assert browser.driver.current_url == exp_url, \
        (f'Wrong url opens after clicking on the forgot password link: '
         f'expected {exp_url}, got {browser.driver.current_url}')


@allure.tag("web")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "suprun")
@allure.epic("Логин пользователя")
@allure.feature("Сброс пароля")
@allure.story("Юзер может перейти в попап сброса пароля")
def test_opens_reset_password_tab_from_login_popup():
    app.open()
    app.header.click_on_sign_in_link()
    app.login_page.open_reset_password_popup()
    reset_password_page = ResetPasswordPage()
    exp_url = f'{config.base_url}{reset_password_page.reset_password_page_link}'

    assert browser.driver.current_url == exp_url, (
        f'Wrong url opens after clicking on the forgot password link: '
        f'expected {exp_url}, got {browser.driver.current_url}')


@allure.tag("web")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "suprun")
@allure.epic("Логин пользователя")
@allure.feature("Сброс пароля")
@allure.story("Юзер может сбросить пароль (используя почту)")
@pytest.mark.skip(reason='Нет инфраструктуры для получения кода подтверждения')
def test_ability_to_change_password(user):
    new_password = 'password123'

    app.open()
    app.header.click_on_sign_in_link()
    app.login_page.open_reset_password_popup()

    app.reset_password_page.type_email(user.email)
    app.popup.submit()

    verification_code = ''
    """
    Получить код, передать его в verification_code = ''
    Ввести его в его поле
    """

    app.reset_password_page.type_verification_code(verification_code)
    app.reset_password_page.type_new_password(new_password)
    user.password = new_password  # задаем новый пароль, чтобы проверить, что он действительно поменялся
    app.popup.submit()
    app.login_page.should_be_logged_in(user.full_name)

    browser.quit()

    app.open()
    app.header.click_on_sign_in_link()
    app.login_page.login_user(user)
    app.login_page.should_be_logged_in(user.full_name)

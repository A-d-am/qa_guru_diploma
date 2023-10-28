from qa_guru_diploma.model.components.header import Header
from qa_guru_diploma.model.pages.registration_page import RegistrationPage
from qa_guru_diploma.model.pages.login_page import LoginPage
from qa_guru_diploma.model.pages.reset_password_page import ResetPasswordPage
from selene import browser
from qa_guru_diploma.data.user import User


# noinspection PyMethodMayBeStatic
class Application:

    def __init__(self):
        self.header = Header()
        self.registration_page = RegistrationPage()
        self.login_page = LoginPage()
        self.reset_password_page = ResetPasswordPage()

    def open(self):
        browser.open('/')

    def open_with_logged_in_user(self, user: User):
        self.open()
        self.header.click_on_sign_in_link()
        self.login_page.login_user(user)


app = Application()

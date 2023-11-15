from selene import browser
from qa_guru_diploma.data.user import User
from qa_guru_diploma.model.components.header import Header
from qa_guru_diploma.model.pages.web.registration_page import RegistrationPage
from qa_guru_diploma.model.pages.web.login_page import LoginPage
from qa_guru_diploma.model.pages.web.reset_password_page import ResetPasswordPage
from qa_guru_diploma.model.pages.mobile.wiki_onboarding_page import WikipediaOnboardingPage
from qa_guru_diploma.model.pages.mobile.wiki_main_page import WikipediaMainPage
from qa_guru_diploma.model.pages.mobile.simple_app_main_page import SimpleAppMainPage


# noinspection PyMethodMayBeStatic
class Application:

    def __init__(self):
        self.header = Header()
        self.registration_page = RegistrationPage()
        self.login_page = LoginPage()
        self.reset_password_page = ResetPasswordPage()
        self.wiki_onboarding_page = WikipediaOnboardingPage()
        self.wiki_main_page = WikipediaMainPage()
        self.simple_app_main_page = SimpleAppMainPage()

    def open(self):
        browser.open('/')

    def open_with_logged_in_user(self, user: User):
        self.open()
        self.header.click_on_sign_in_link()
        self.login_page.login_user(user)


app = Application()

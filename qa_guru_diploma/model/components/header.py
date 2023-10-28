from selene import browser, have, be


# noinspection PyMethodMayBeStatic
class Header:

    def __init__(self):
        self.search_field = browser.element('.js_header_search_field')
        self.serp = browser.all('.os-content').first
        self.chosen_language = browser.element('.header_main_language')

    def click_on_logo(self):
        browser.element('.logo').click()

    def click_on_search_field(self):
        try:
            self.search_field.click()
        except:
            self.search_field.click()

    def type_to_search_field(self, value):
        self.search_field.should(be.blank).type(value)

    def click_on_element_in_serp(self, value):
        self.serp.all('.item').element('.title').should(have.text(value)).click()


    def search(self, value):
        self.click_on_search_field()
        self.type_to_search_field(value)
        self.click_on_element_in_serp(value)

    def element_should_be_in_serp(self, value):
        self.serp.all('.item').element('.title').should(have.text(value))

    def click_on_chosen_language(self):
        self.chosen_language.click()

    def set_language(self, value):
        self.click_on_chosen_language()
        browser.all('.header_main_language li .label').element_by(have.exact_text(value)).click()

    def click_on_registration_link(self):
        browser.element('#js_header_demo_registration').click()

    def click_on_sign_in_link(self):
        browser.element('#js_header_demo_login').click()

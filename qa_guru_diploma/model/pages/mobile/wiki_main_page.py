from selene import browser, have, be
import allure
from appium.webdriver.common.appiumby import AppiumBy


# noinspection PyMethodMayBeStatic
class WikipediaMainPage:

    def get_search_results(self):
        search_results = browser.all((AppiumBy.ID, 'org.wikipedia:id/page_list_item_title'))
        return search_results

    def type_to_search(self, value):
        with allure.step(f'Нажимаем на поиск и вводим {value}'):
            browser.element((AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia")).click()
            browser.element((AppiumBy.ID, "org.wikipedia:id/search_src_text")).type(value)

    def verify_content_found(self, value):
        with allure.step(f'Проверяем, что в поисковой выдаче есть {value}'):
            results = self.get_search_results()
            results.should(have.size_greater_than(0))
            results.first.should(have.text(value))

    def open_article(self, ordinal=1):
        with allure.step(f'Открываем {ordinal} статью в поисковой выдаче'):
            search_results = self.get_search_results()
            ordinal = ordinal - 1
            if ordinal < 0:
                search_results.first.click()
            else:
                search_results[ordinal].click()

    def article_is_opened(self, value):
        with allure.step(f'Страница статьи {value} открыта'):
            article_header = browser.element((AppiumBy.CLASS_NAME, "android.widget.TextView"))
            assert article_header.should(have.exact_text(value))

    def verify_main_page_is_opened(self):
        with allure.step('Проверяем, что открыта главный экран приложения'):
            browser.element((AppiumBy.ID, 'org.wikipedia:id/main_toolbar_wordmark')).should(be.visible)

    def click_on_accept_send_anon_data(self):
        with allure.step(''):
            browser.element((AppiumBy.ID, 'org.wikipedia:id/acceptButton')).click()

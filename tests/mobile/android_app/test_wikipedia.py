import pytest
from tests.conftest import android
from qa_guru_diploma.application import app


@android
def test_search():
    text_to_search = 'Appium'
    app.wiki_onboarding_page.click_on_skip_button()
    app.wiki_main_page.verify_main_page_is_opened()

    app.wiki_main_page.type_to_search(text_to_search)

    app.wiki_main_page.verify_content_found(text_to_search)


@android
def test_open_article_after_search():
    text_to_search = 'Appium'
    app.wiki_onboarding_page.click_on_skip_button()

    app.wiki_main_page.type_to_search(text_to_search)
    app.wiki_main_page.verify_content_found(text_to_search)
    app.wiki_main_page.open_article(1)

    app.wiki_main_page.article_is_opened(text_to_search)


@android
def test_onboarding_steps_titles():
    app.wiki_onboarding_page.verify_screen_title_text(onboarding_step=1, expected_title_text='The Free Encyclopedia')
    app.wiki_onboarding_page.verify_screen_text()

    app.wiki_onboarding_page.verify_screen_title_text(onboarding_step=2, expected_title_text='New ways to explore')
    app.wiki_onboarding_page.click_on_continue_button()

    app.wiki_onboarding_page.verify_screen_title_text(onboarding_step=3, expected_title_text='Reading lists with sync')
    app.wiki_onboarding_page.click_on_continue_button()

    app.wiki_onboarding_page.verify_screen_title_text(onboarding_step=4, expected_title_text='Send anonymous data')
    app.wiki_onboarding_page.click_on_accept_send_anon_data()

    app.wiki_main_page.verify_main_page_is_opened()


@android
@pytest.mark.parametrize('step_number, expected_title_text',
                         [
                             pytest.param(1, 'The Free Encyclopedia', id='First onboarding step'),
                             pytest.param(2, 'New ways to explore', id='Second onboarding step'),
                             pytest.param(3, 'Reading lists with sync', id='Third onboarding step'),
                             pytest.param(4, 'Send anonymous data', id='Final onboarding step'),

                         ]
                         )
def test_ability_skip_onboarding_from_step(step_number, expected_title_text):
    app.wiki_onboarding_page.open_article(step_number)

    app.wiki_onboarding_page.verify_screen_title_text(onboarding_step=step_number,
                                                      expected_title_text=expected_title_text)

    app.wiki_main_page.verify_main_page_is_opened()


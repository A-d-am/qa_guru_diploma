import allure
import pytest
from allure_commons.types import Severity
from tests import conftest
from qa_guru_diploma.application import app
from tests.conftest import project_config


@allure.tag("ios")
@allure.severity(Severity.NORMAL)
@allure.label("owner", "suprun")
@allure.epic("Mobile тесты")
@allure.feature("Sample app iOS")
@allure.story(f"Проверяем, что в Text Output отображается введенный в Text Input текст")
@conftest.ios
@pytest.mark.ios
def test_text_button():
    text_to_input = 'Hello,world!'
    app.simple_app_main_page.click_on_text_button()
    app.simple_app_main_page.click_on_text_input_field()
    app.simple_app_main_page.type_into_text_input_field(text_to_input)

    app.simple_app_main_page.expected_text_is_in_output(text_to_input)


@allure.tag("ios")
@allure.severity(Severity.NORMAL)
@allure.label("owner", "suprun")
@allure.epic("Mobile тесты")
@allure.feature("Sample app iOS")
@allure.story(f"Проверяем, что по нажатию на Alert вызывается alert")
@conftest.ios
@pytest.mark.ios
def test_alert():
    app.simple_app_main_page.click_on_alert_button()

    app.simple_app_main_page.click_on_ok_button_in_alert()

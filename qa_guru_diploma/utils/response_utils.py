import requests
import jsonschema
from allure_commons.types import AttachmentType
import allure


def check_status_code(expected_code, response):
    with allure.step(f'Проверяем, что пришел status code = {expected_code}'):
        assert response.status_code == expected_code, \
            f'Пришел неверный статус код: ожидался {expected_code}, пришел {response.status_code}'


def check_response_json_schema(expected_schema, response):
    with allure.step('Проверяем содержание response.json'):
        try:
            jsonschema.validate(response.json(), expected_schema)
        except requests.exceptions.JSONDecodeError:
            allure.attach(
                body=str(response.status_code),
                name='status_code',
                attachment_type=AttachmentType.TEXT,
                extension='txt'
            )

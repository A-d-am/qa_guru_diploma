import requests
import jsonschema
from allure_commons.types import AttachmentType
import allure


def check_status_code(expected_status_code, response_status_code):
    with allure.step(f'Проверяем, что пришел status code = {expected_status_code}'):
        assert response_status_code == expected_status_code, (f'Wrong response status code: '
                                                              f'expected status code = {expected_status_code}, '
                                                              f'got {response_status_code}')


def validate_response_json(expected_schema, response):
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

from qa_guru_diploma.utils.schema import load_schema
from qa_guru_diploma.utils import response_utils
from allure_commons.types import AttachmentType
from requests import sessions
from curlify import to_curl
import allure
import json


def github_api(method, url, **kwargs):
    args = kwargs
    base_url = 'https://api.github.com'
    new_url = base_url + url
    method = method.upper()
    with allure.step(f'Отправляем запрос {method} {url} {args if len(args) != 0 else ""} '):
        with sessions.Session() as session:
            response = session.request(method=method, url=new_url, **kwargs)
            message = to_curl(response.request)
            allure.attach(body=message.encode('utf8'), name='Curl', attachment_type=AttachmentType.TEXT,
                          extension='txt')
            allure.attach(body=json.dumps(response.json(), indent=4).encode("utf8"), name="Response Json",
                          attachment_type=AttachmentType.JSON, extension='json')
    return response



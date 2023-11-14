from selenium import webdriver as selenium_webdriver
from appium import webdriver as appium_webdriver
from selene import browser
import pytest
import allure
from qa_guru_diploma.data.user import User
from qa_guru_diploma.data import user_data
from qa_guru_diploma import utils
from qa_guru_diploma.utils import allure_utils
import project


@pytest.fixture(scope='function')
def user():
    user = User(
        full_name=user_data.user_full_name,
        email=user_data.user_login_email,
        phone=user_data.user_login_phone,
        password=user_data.user_password
    )
    return user


project_config = project.Config(_env_file=utils.file.relative_from_root(f'.env.{project.Config().context}'))


@pytest.fixture(scope='function', autouse=True)
def driver_management(request):
    with allure.step('init session'):
        if request.param == 'web' or 'api':
            browser.config.base_url = project_config.base_url
            browser.config.driver_options = project_config.driver_options(request.param)
            browser.config.window_height = 1080
            browser.config.window_width = 1920

        elif request.param == 'ios' or 'android':
            browser.config.driver = appium_webdriver.Remote(
                project_config.driver_remote_url, options=project_config.driver_options(request.param)
            )

    yield

    if project_config.context == 'web':
        allure_utils.attach_html(browser)
        allure_utils.attach_web_logs(browser)
        allure_utils.attach_video(browser)
    #TODO: добавить api аттачи
    allure_utils.attach_screenshot(browser)

    session_id = browser.driver.session_id

    if project_config.context in ['bstack', 'local_emulator', 'local_real']:
        allure_utils.attach_mobile_page_source(browser)

    with allure.step('tear down app session with id: ' + session_id):
        browser.quit()

    if project_config.is_bstack_run(request.param):
        allure_utils.attach_bstack_video(session_id, project_config.bstack_userName, project_config.bstack_accessKey)


ios = pytest.mark.parametrize('driver_management', ['ios'], indirect=True)
android = pytest.mark.parametrize('driver_management', ['android'], indirect=True)
api = pytest.mark.parametrize('driver_management', ['api'], indirect=True)
web = pytest.mark.parametrize('driver_management', ['web'], indirect=True)

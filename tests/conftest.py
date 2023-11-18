from selenium import webdriver as selenium_webdriver
from appium import webdriver as appium_webdriver
from selene import browser, support
import pytest
import allure
import allure_commons
from qa_guru_diploma import utils
from qa_guru_diploma.utils import allure_utils
import project

project_config = project.Config(_env_file=utils.file.relative_from_root(
    f'.env.{project.Config().context}') if project.Config().context != 'api' else '')


@pytest.fixture(scope='function', autouse=True)
def driver_management(request):
    if request.param in ['ios', 'android']:
        with allure.step('init app session'):
            browser.config.driver = appium_webdriver.Remote(
                project_config.driver_remote_url, options=project_config.driver_options(request.param)
            )

        browser.config.timeout = project_config.timeout
        browser.config._wait_decorator = support._logging.wait_with(
            context=allure_commons._allure.StepContext
        )

    elif request.param == 'web':
        browser.config.base_url = project_config.base_url
        browser.config.window_height = 1080
        browser.config.window_width = 1920

        driver = selenium_webdriver.Remote(
            command_executor=project_config.get_selenoid_link(),
            options=project_config.driver_options(request.param)
        )
        browser.config.driver = driver

    elif request.param == 'api':
        with allure.step('Start api test'):
            pass

    yield

    if request.param == 'web':
        allure_utils.attach_html(browser)
        allure_utils.attach_web_logs(browser)
        allure_utils.attach_video(browser)
        allure_utils.attach_screenshot(browser)

    if project_config.context in ['bstack', 'local_emulator', 'local_real']:
        allure_utils.attach_mobile_page_source(browser)

    if project_config.context != 'api':
        session_id = browser.driver.session_id
    else:
        session_id = ''

    if project_config.context != 'api':
        with allure.step('tear down app session with id: ' + session_id):
            browser.quit()

    if project_config.context == 'bstack':
        allure_utils.attach_bstack_video(session_id, project_config.bstack_userName,
                                         project_config.bstack_accessKey)


ios = pytest.mark.parametrize('driver_management', ['ios'], indirect=True)
android = pytest.mark.parametrize('driver_management', ['android'], indirect=True)
api = pytest.mark.parametrize('driver_management', ['api'], indirect=True)
web = pytest.mark.parametrize('driver_management', ['web'], indirect=True)

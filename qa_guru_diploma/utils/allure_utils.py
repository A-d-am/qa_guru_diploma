import allure
from allure_commons.types import AttachmentType
import requests


def attach_screenshot(browser):
    png = browser.driver.get_screenshot_as_png()
    allure.attach(
        body=png,
        name='screenshot',
        attachment_type=allure.attachment_type.PNG,
        extension='.png',
    )


def attach_web_logs(browser):
    log = "".join(f'{text}\n' for text in browser.driver.get_log(log_type='browser'))
    allure.attach(
        body=log,
        name='browser_logs',
        attachment_type=allure.attachment_type.TEXT,
        extension='.log'
    )


def attach_html(browser):
    html = browser.driver.page_source
    allure.attach(
        body=html,
        name='page_source',
        attachment_type=AttachmentType.HTML,
        extension='.html'
    )


def attach_video(browser):
    video_url = "https://selenoid.autotests.cloud/video/" + browser.driver.session_id + ".mp4"
    html = "<html><body><video width='100%' height='100%' controls autoplay><source src='" \
           + video_url \
           + "' type='video/mp4'></video></body></html>"
    allure.attach(
        body=html,
        name='video_' + browser.driver.session_id,
        attachment_type=allure.attachment_type.HTML,
        extension='.html'
    )


def attach_bstack_video(session_id, bstack_userName, bstack_accessKey):
    bstack_session = requests.get(
        f'https://api.browserstack.com/app-automate/sessions/{session_id}.json',
        auth=(bstack_userName, bstack_accessKey),
    ).json()

    video_url = bstack_session['automation_session']['video_url']

    allure.attach(
        '<html><body>'
        '<video width="100%" height="100%" controls autoplay>'
        f'<source src="{video_url}" type="video/mp4">'
        '</video>'
        '</body></html>',
        name='mobile video recording ' + session_id,
        attachment_type=allure.attachment_type.HTML,
    )


def attach_mobile_page_source(browser):
    allure.attach(
        browser.driver.page_source,
        name='screen xml dump',
        attachment_type=allure.attachment_type.XML,
    )

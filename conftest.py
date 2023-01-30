import pytest
from selene.support.shared import browser


@pytest.fixture(scope="function", autouse=True)
def open_browser():
    browser.config.window_width = 1080
    browser.config.window_width = 1080
    browser.config.base_url = 'https://playground.learnqa.ru'

    yield

    browser.quit()


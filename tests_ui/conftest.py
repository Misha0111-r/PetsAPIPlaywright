from typing import Generator

import pytest
from playwright.sync_api import Playwright, APIRequestContext

from pages.login_page import LoginPage
from config import LoginPageConfig


@pytest.fixture(scope='session')
def login(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    login_page = LoginPage(page)
    login_page.open_page(LoginPageConfig.LOGIN_PAGE_URL)
    login_page.fill_login_field(LoginPageConfig.EMAIL)
    login_page.fill_password_field(LoginPageConfig.PASSWORD)
    login_page.click_submit_button()
    login_page.check_profile_page(LoginPageConfig.PROFILE_PAGE_URL)
    return page

@pytest.fixture(scope="session")
def api_request_context(
    playwright: Playwright,
) -> Generator[APIRequestContext, None, None]:
    request_context = playwright.request.new_context(
        base_url="http://34.141.58.52:8000/"
    )
    yield request_context
    request_context.dispose()

import pytest

from pages.login_page import LoginPage
from config import LoginPageConfig


@pytest.mark.ui
@pytest.mark.positive
class TestLogin:

    def test_login(self, page):
        login_page = LoginPage(page)
        login_page.open_page(LoginPageConfig.LOGIN_PAGE_URL)
        login_page.fill_login_field(LoginPageConfig.EMAIL)
        login_page.fill_password_field(LoginPageConfig.PASSWORD)
        login_page.click_submit_button()
        login_page.check_profile_page(LoginPageConfig.PROFILE_PAGE_URL)


@pytest.mark.ui
@pytest.mark.negative
class TestLoginNegative:

    @pytest.mark.parametrize('email', ['a', '@gmail.com'])
    def test_login_invalid_email(self, page, email):
        login_page = LoginPage(page)
        login_page.open_page(LoginPageConfig.LOGIN_PAGE_URL)
        login_page.fill_login_field(email)
        login_page.click_submit_button()
        login_page.check_invalid_email_message()

    def test_login_empty_password(self, page):
        login_page = LoginPage(page)
        login_page.open_page(LoginPageConfig.LOGIN_PAGE_URL)
        login_page.fill_login_field(LoginPageConfig.EMAIL)
        login_page.click_submit_button()
        login_page.check_empty_password_message()

    @pytest.mark.parametrize('email, password', [('a', ''), ('@gmail.com', '2'), ('a@gmail.com', '')])
    def test_login_invalid_data(self, page, email, password):
        login_page = LoginPage(page)
        login_page.open_page(LoginPageConfig.LOGIN_PAGE_URL)
        login_page.fill_login_field(email)
        login_page.fill_password_field(password)
        login_page.click_submit_button()
        if '@gmail.com' not in email:
            login_page.check_invalid_email_message()
        if password == '':
            login_page.check_empty_password_message()
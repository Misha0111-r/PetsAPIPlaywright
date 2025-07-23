from playwright.sync_api import expect
from pages.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.LOGIN_FIELD = self.page.locator('//*[@id="login"]')
        self.PASSWORD_FIELD = self.page.locator('//*[@id="password"]/input')
        self.SUBMIT_BUTTON = self.page.get_by_text('Submit')
        self.INVALID_EMAIL_MESSAGE = self.page.get_by_text('This field is email')
        self.EMPTY_PASSWORD_MESSAGE = self.page.get_by_text('This field is required')

    def fill_login_field(self, login):
        self.LOGIN_FIELD.fill(login)

    def fill_password_field(self, password):
        self.PASSWORD_FIELD.fill(password)
        self.LOGIN_FIELD.click()

    def click_submit_button(self):
        self.SUBMIT_BUTTON.click()

    def check_profile_page(self, link):
        expect(self.page).to_have_url(link)

    def check_invalid_email_message(self):
        expect(self.INVALID_EMAIL_MESSAGE).to_be_visible()

    def check_empty_password_message(self):
        expect(self.EMPTY_PASSWORD_MESSAGE).to_be_visible()

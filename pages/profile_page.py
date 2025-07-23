from playwright.sync_api import expect

from pages.base_page import BasePage


class ProfilePage(BasePage):

    def __init__(self, page):
        super().__init__(page)
        self.ADD_PET_BUTTON = self.page.locator('//*[@id="app"]/main/div/div/div[1]/div/div[1]/button/span[1]')
        self.NAME_FIELD = self.page.locator('//*[@id="name"]')
        self.AGE_FIELD = self.page.locator('//*[@id="age"]/input')
        self.TYPE_DROPDOWN = self.page.locator('//*[@id="typeSelector"]')
        self.GENDER_DROPDOWN = self.page.locator('//*[@id="genderSelector"]')
        self.SUBMIT_BUTTON = self.page.locator('//*[@id="app"]/main/div/div/form/div/div[2]/div[3]/button[1]/span[2]')
        self.CHOOSE_IMAGE_BUTTON = self.page.locator('//*[@id="app"]/main/div/div/div[2]/div[2]/div/span')
        self.EDIT_BUTTON = self.page.get_by_text('Edit')
        self.DELETE_BUTTON = self.page.get_by_text('Delete')
        self.SUBMIT_DELETE_BUTTON = self.page.get_by_text('Yes')
        self.SAVE_BUTTON = self.page.locator('//*[@id="app"]/main/div/form/div/div[2]/div[3]/button')

    def click_add_pet_button(self):
        self.ADD_PET_BUTTON.click()

    def fill_name_field(self, name):
        self.NAME_FIELD.fill(name)
        self.NAME_FIELD.press('X')

    def fill_age_field(self, age):
        self.AGE_FIELD.fill(age)

    def click_type_dropdown(self):
        self.TYPE_DROPDOWN.click()

    def select_type(self, pet_type):
        self.page.locator(f'//li[text()="{pet_type}"]').click()

    def click_gender_dropdown(self):
        self.GENDER_DROPDOWN.click()

    def click_submit_button(self):
        self.SUBMIT_BUTTON.click()

    def click_choose_image_button(self):
        self.CHOOSE_IMAGE_BUTTON.click()

    def check_add_pet_page(self, link):
        expect(self.page).to_have_url(link)

    def click_last_edit_button(self):
        amount = self.EDIT_BUTTON.count()
        self.EDIT_BUTTON.nth(amount-1).click()

    def click_last_delete_button(self):
        amount = self.DELETE_BUTTON.count()
        self.DELETE_BUTTON.nth(amount-1).click()
        self.SUBMIT_DELETE_BUTTON.click()

    def click_save_button(self):
        self.SAVE_BUTTON.click()

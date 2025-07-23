import random
import string

import allure
import pytest

from config import AddPetPageConfig
from pages.profile_page import ProfilePage
from clients.client import Client
from models.pet_models import GetResponseModel, PetResponseModel
from playwright.sync_api import APIRequestContext
import generator


@pytest.mark.ui
class TestProfilePage:

    @pytest.mark.dependency(name='test_add_pet')
    @pytest.mark.parametrize('gender', ['Male', 'Female'])
    def test_add_pet(self, api_request_context, login, gender):
        add_pet_page = ProfilePage(login)
        with allure.step('open profile page'):
            add_pet_page.open_page(AddPetPageConfig.PROFILE_PAGE_URL)
        with allure.step('click add pet button'):
            add_pet_page.click_add_pet_button()
        with allure.step('create new name'):
            new_name = ''.join([random.choice(string.ascii_letters) for _ in range(5)])
        with allure.step(f'fill name field with {new_name}'):
            add_pet_page.fill_name_field(new_name)
        with allure.step('create new age'):
            new_age = str(random.randrange(0, 25))
        with allure.step(f'fill age field with {new_age}'):
            add_pet_page.fill_age_field(new_age)
        with allure.step('click dropdown button with pet type choice'):
            add_pet_page.click_type_dropdown()
        with allure.step('select pet type'):
            add_pet_page.select_type('cat')
        with allure.step('click dropdown button with gender choice'):
            add_pet_page.click_gender_dropdown()
        with allure.step('select pet gender'):
            add_pet_page.select_type('Female')
        with allure.step('click submit button'):
            add_pet_page.click_submit_button()
        with allure.step('set pet image'):
            login.set_input_files('input[type="file"]', AddPetPageConfig.CUTE_CAT_IMAGE_PATH)
        with allure.step('click button to submit pet image'):
            add_pet_page.click_choose_image_button()
        with allure.step('check final page'):
            add_pet_page.check_add_pet_page(AddPetPageConfig.PROFILE_PAGE_URL)
        with allure.step('click edit button from last pet'):
            add_pet_page.click_last_edit_button()
        with allure.step('check pet through api'):
            pet_id = add_pet_page.get_pet_id_from_page()
            expected_model = GetResponseModel(pet=PetResponseModel(id=pet_id))
            Client().get_pet(api_request_context, pet_id, expected_model)
        with allure.step('go to profile page'):
            add_pet_page.open_page(AddPetPageConfig.PROFILE_PAGE_URL)
        with allure.step('delete new created pets'):
            add_pet_page.click_last_delete_button()

    @pytest.mark.dependency(depends='test_add_pet')
    @pytest.mark.parametrize('pet_type', ['dog', 'reptile'])
    def test_edit_pet(self, api_request_context, login, pet_type):
        edit_pet_page = ProfilePage(login)
        with allure.step('open profile page'):
            edit_pet_page.open_page(AddPetPageConfig.PROFILE_PAGE_URL)
        with allure.step('click edit button from last pet'):
            edit_pet_page.click_last_edit_button()
        with allure.step('create new name'):
            new_name = generator.random_name(5)
        with allure.step(f'fill name field with {new_name}'):
            edit_pet_page.fill_name_field(new_name)
        with allure.step('click dropdown button with pet type choice'):
            edit_pet_page.click_type_dropdown()
        with allure.step('select pet type'):
            edit_pet_page.select_type(pet_type)
        with allure.step('click save button'):
            edit_pet_page.click_save_button()
        with allure.step('check final page'):
            edit_pet_page.check_add_pet_page(AddPetPageConfig.SAVED_PET_PROFILE_URL)
        with allure.step('click edit button from last pet'):
            edit_pet_page.click_last_edit_button()
        with allure.step('check pet through api'):
            pet_id = edit_pet_page.get_pet_id_from_page()
            expected_model = GetResponseModel(pet=PetResponseModel(id=pet_id, name=new_name, type=pet_type))
            Client().get_pet(api_request_context, pet_id, expected_model)

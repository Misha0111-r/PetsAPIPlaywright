from typing import Union

import allure
from models.pet_models import LoginModel, LoginRegisterResponseModel, PostPetModel, GeneralResponseModel, \
    UpdatePetModel, \
    AddCommentModel, GetResponseModel, LoginRegisterNegativeResponseModel, RegisterModel
from playwright.sync_api import APIRequestContext
from pydantic import BaseModel


class ClientApi:
    def __init__(self):
        self.base_url = 'http://34.141.58.52:8000/'

    def validate_model(self, response, expected_model, status_code):
        assert response.status == status_code
        for i in expected_model:
            print(type(i[1]))
            if i[1] is None or isinstance(i[1], BaseModel):
                continue
            else:
                assert i[1] == response.json()[i[0]]
        return expected_model.model_validate(response.json())


class Client(ClientApi):
    def __init__(self):
        super().__init__()

    @allure.step('POST /login')
    def login(self, api_request_context: APIRequestContext, request: LoginModel, expected_model: Union[LoginRegisterResponseModel, LoginRegisterNegativeResponseModel], status_code: int = 200):
        response = api_request_context.post(f"/login", data=request.model_dump())
        return self.validate_model(response, expected_model, status_code)

    @allure.step('POST /pet')
    def post_pet(self, api_request_context: APIRequestContext, login, request: PostPetModel, expected_model: GeneralResponseModel, status_code: int = 200):
        headers = {'Authorization': f'Bearer {login["token"]}'}
        response = api_request_context.post(f"/pet", data=request.model_dump(), headers=headers)
        return self.validate_model(response, expected_model, status_code)

    @allure.step('PATCH /pet')
    def update_pet_info(self, api_request_context: APIRequestContext, login, request: UpdatePetModel, expected_model: GeneralResponseModel, status_code: int = 200):
        headers = {'Authorization': f'Bearer {login["token"]}'}
        response = api_request_context.patch(f"/pet", data=request.model_dump(), headers=headers)
        return self.validate_model(response, expected_model, status_code)

    @allure.step('PUT /pet/id/comment')
    def add_comment(self, api_request_context: APIRequestContext, login, request: AddCommentModel, expected_model: GeneralResponseModel, status_code: int = 200):
        headers = {'Authorization': f'Bearer {login["token"]}'}
        response = api_request_context.put(f"/pet/{request.pet_id}/comment", data=request.model_dump(), headers=headers)
        return self.validate_model(response, expected_model, status_code)

    @allure.step('GET /pet/id')
    def get_pet(self, api_request_context: APIRequestContext, pet_id: int, expected_model: GetResponseModel, status_code: int = 200):
        response = api_request_context.get(f"pet/{pet_id}", data=None)
        return self.validate_model(response, expected_model, status_code)

    @allure.step('POST /register')
    def register(self, api_request_context: APIRequestContext, request: RegisterModel, expected_model: Union[LoginRegisterResponseModel, LoginRegisterNegativeResponseModel], status_code: int = 200):
        response = api_request_context.post(f"/register", data=request.model_dump())
        return self.validate_model(response, expected_model, status_code)
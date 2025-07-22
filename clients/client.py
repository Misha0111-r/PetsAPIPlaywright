import allure
import requests

from allure_helper import AllureHelper
from config import LoginPageConfig
from models.pet_models import LoginModel, LoginResponseModel, PostPetModel, GeneralResponseModel, UpdatePetModel, \
    AddCommentModel, GetResponseModel


class ClientApi:
    def __init__(self):
        self.base_url = 'http://34.141.58.52:8000/'
        self.session = self._initialize_session()

    @staticmethod
    def _initialize_session():
        return requests.Session()

    def request(self, method: str, url: str, json, headers: dict={}):
        response = self.session.request(method=method, url=self.base_url+url, json=json, headers=headers)
        AllureHelper().enrich_allure(response)
        return response

    @staticmethod
    def validate_model(response, expected_model, status_code):
        assert status_code == response.status_code
        return expected_model.model_validate(response.json())


class Client(ClientApi):
    def __init__(self):
        super().__init__()

    @allure.step('POST /login')
    def login(self, request: LoginModel, expected_model: LoginResponseModel, status_code: int = 200):
        response = self.request(method='post', url='login', json=request.model_dump())
        return self.validate_model(response, expected_model, status_code), response.json()

    @allure.step('POST /pet')
    def post_pet(self, login, request: PostPetModel, expected_model: GeneralResponseModel, status_code: int = 200):
        headers = {'Authorization': f'Bearer {login["token"]}'}
        response = self.request(method='post', url='pet', json=request.model_dump(), headers=headers)
        return self.validate_model(response, expected_model, status_code)

    @allure.step('PATCH /pet')
    def update_pet_info(self, login, request: UpdatePetModel, expected_model: GeneralResponseModel, status_code: int = 200):
        headers = {'Authorization': f'Bearer {login["token"]}'}
        response = self.request(method='post', url='pet', json=request.model_dump(), headers=headers)
        return self.validate_model(response, expected_model, status_code)

    @allure.step('PUT /pet/id/comment')
    def add_comment(self, login, request: AddCommentModel, expected_model: GeneralResponseModel, status_code: int = 200):
        headers = {'Authorization': f'Bearer {login["token"]}'}
        response = self.request(method='put', url=f'pet/{request.pet_id}/comment', json=request.model_dump(), headers=headers)
        return self.validate_model(response, expected_model, status_code)

    @allure.step('GET /pet/id')
    def get_pet(self, pet_id: int, expected_model: GetResponseModel, status_code: int = 200):
        response = self.request(method='get', url=f'pet/{pet_id}', json=None)
        return self.validate_model(response, expected_model, status_code)

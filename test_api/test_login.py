import pytest
from playwright.sync_api import APIRequestContext

from clients.client import Client
from config import LoginPageConfig
from models.pet_models import LoginModel, LoginRegisterResponseModel, LoginRegisterNegativeResponseModel


@pytest.mark.api
@pytest.mark.positive
class TestLoginPage:

    def test_login(self, api_request_context: APIRequestContext) -> None:
        request = LoginModel(email=LoginPageConfig.EMAIL, password=LoginPageConfig.PASSWORD)
        expected_model = LoginRegisterResponseModel(email=LoginPageConfig.EMAIL)
        Client().login(api_request_context ,request, expected_model)

@pytest.mark.api
@pytest.mark.negative
class TestLoginPageNegative:

    @pytest.mark.parametrize('password', ['', '123'])
    def test_login_incorrect_password(self, api_request_context, password):
        request = LoginModel(email=LoginPageConfig.EMAIL, password=password)
        expected_model = LoginRegisterNegativeResponseModel(detail='Username is taken or pass issue')
        Client().login(api_request_context, request, expected_model, 400)

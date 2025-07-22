import random
import string

import pytest
from playwright.sync_api import APIRequestContext

from clients.client import Client
from config import LoginPageConfig
from models.pet_models import LoginModel, LoginRegisterResponseModel, LoginRegisterNegativeResponseModel, RegisterModel


@pytest.mark.api
@pytest.mark.positive
class TestRegisterPage:

    def test_register(self, api_request_context: APIRequestContext) -> None:
        email = ''.join(random.choice(string.ascii_letters) for _ in range(5)) + '@gmail.com'
        request = RegisterModel(email=email, password=LoginPageConfig.PASSWORD, confirm_password=LoginPageConfig.PASSWORD)
        expected_model = LoginRegisterResponseModel(email=email)
        Client().register(api_request_context, request, expected_model)

@pytest.mark.api
@pytest.mark.negative
class TestRegisterPageNegative:

    @pytest.mark.parametrize('email, password', [('@' , '23d32mo'), ('', 'cwmd313*'), ('21d2dm@gmail.com' ,'')])
    def test_register_invalid_data(self, api_request_context, email, password):
        request = RegisterModel(email=email, password=password, confirm_password=password)
        expected_model = LoginRegisterNegativeResponseModel(detail='Username is taken or pass issue')
        Client().register(api_request_context, request, expected_model, 400)
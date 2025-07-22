import json

import pytest
from typing import Generator

import pytest
from playwright.sync_api import Playwright, APIRequestContext

from clients.client import Client
from config import LoginPageConfig
from models.pet_models import LoginModel, LoginRegisterResponseModel


@pytest.fixture(scope='session')
def login(api_request_context: APIRequestContext) -> json:
    request = LoginModel(email=LoginPageConfig.EMAIL, password=LoginPageConfig.PASSWORD)
    expected_model = LoginRegisterResponseModel(email=LoginPageConfig.EMAIL)
    return Client().login(api_request_context, request, expected_model).model_dump()

@pytest.fixture(scope="session")
def api_request_context(
    playwright: Playwright,
) -> Generator[APIRequestContext, None, None]:
    request_context = playwright.request.new_context(
        base_url="http://34.141.58.52:8000/"
    )
    yield request_context
    request_context.dispose()

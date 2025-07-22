import pytest
from typing import Generator

import pytest
from playwright.sync_api import Playwright, APIRequestContext


@pytest.fixture(scope='session')
def login():
    # request = LoginModel(email=LoginPageConfig.EMAIL, password=LoginPageConfig.PASSWORD)
    # response = ClientApi().request(method='post', url='login', json=request.model_dump())
    # return response.json()
    pass

@pytest.fixture(scope="session")
def api_request_context(
    playwright: Playwright,
) -> Generator[APIRequestContext, None, None]:
    request_context = playwright.request.new_context(
        base_url="http://34.141.58.52:8000/"
    )
    yield request_context
    request_context.dispose()

import pytest
from playwright.sync_api import APIRequestContext
from config import LoginPageConfig
from models.pet_models import LoginModel, LoginResponseModel


@pytest.mark.api
def test_login(api_request_context: APIRequestContext) -> None:
    request = LoginModel(email=LoginPageConfig.EMAIL, password=LoginPageConfig.PASSWORD)
    new_login = api_request_context.post(f"/login", data=request.model_dump())
    assert new_login.ok
    response = new_login.json()
    print(response)
    expected_model = LoginResponseModel(email='Aboba')
    print(expected_model.model_validate(response))


# @pytest.mark.api
# def test_should_create_feature_request(api_request_context: APIRequestContext) -> None:
#     data = {
#         "title": "[Feature] request 1",
#         "body": "Feature description",
#     }
#     new_issue = api_request_context.post(f"/repos/{GITHUB_USER}/{GITHUB_REPO}/issues", data=data)
#     assert new_issue.ok
#
#     issues = api_request_context.get(f"/repos/{GITHUB_USER}/{GITHUB_REPO}/issues")
#     assert issues.ok
#     issues_response = issues.json()
#     issue = list(filter(lambda issue: issue["title"] == "[Feature] request 1", issues_response))[0]
#     assert issue
#     assert issue["body"] == "Feature description"
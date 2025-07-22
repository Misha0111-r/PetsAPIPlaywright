import pytest

from clients.client import Client
from models.pet_models import PostPetModel, GeneralResponseModel, UpdatePetModel, AddCommentModel


@pytest.mark.api
@pytest.mark.positive
class TestProfilePage:

    def test_post_pet(self, api_request_context, login):
        request = PostPetModel(name='boba', type='cat', age=14, gender='Male')
        expected_model = GeneralResponseModel()
        Client().post_pet(api_request_context, login, request, expected_model)

    def test_update_pet_info(self, api_request_context, login):
        request = UpdatePetModel(id=35057, name='DemoRenamed', type='NewType', age=33, gender='Male')
        expected_model = GeneralResponseModel(id=35057)
        Client().update_pet_info(api_request_context, login, request, expected_model)

    def test_add_comment(self, api_request_context, login):
        request = AddCommentModel(pet_id=35057, message='I love you!')
        expected_model = GeneralResponseModel()
        Client().add_comment(api_request_context,login, request, expected_model)

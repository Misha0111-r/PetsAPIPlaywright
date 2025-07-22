# import pytest
#
# from clients.client import Client
# from models.pet_models import PostPetModel, GeneralResponseModel, UpdatePetModel, AddCommentModel
#
#
# @pytest.mark.api
# class TestProfilePage:
#
#     def test_post_pet(self, login):
#         request = PostPetModel(name='boba', type='cat', age=14, gender='Male')
#         expected_model = GeneralResponseModel()
#         Client().post_pet(login, request, expected_model)
#
#     def test_update_pet_info(self, login):
#         request = UpdatePetModel(id=35057, name='DemoRenamed', type='NewType', age=33, gender='Male')
#         expected_model = GeneralResponseModel(id=35057)
#         Client().update_pet_info(login, request, expected_model)
#
#     def test_add_comment(self, login):
#         request = AddCommentModel(pet_id=35057, message='I love you!')
#         expected_model = GeneralResponseModel()
#         Client().add_comment(login, request, expected_model)

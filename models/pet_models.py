from typing import Optional
from pydantic import BaseModel


class LoginModel(BaseModel):
    email: str
    password: str


class LoginResponseModel(BaseModel):
    token: Optional[str] = None
    email: Optional[str] = None
    id: Optional[int] = None


class PostPetModel(BaseModel):
    pet_id: int = 0
    name: str
    type: str
    age: int
    gender: str
    owner_id: int = 4358


class UpdatePetModel(BaseModel):
    id: int
    name: str
    type: str
    age: int
    gender: str


class AddCommentModel(BaseModel):
    pet_id: Optional[int] = None
    message: Optional[str] = None


class GeneralResponseModel(BaseModel):
    id: Optional[int] = None


class PetResponseModel(BaseModel):
    id: int
    name: Optional[str] = None
    type: Optional[str] = None
    age: Optional[int] = None
    gender: Optional[str] = None
    owner_id: Optional[int] = None
    pic: Optional[str] = None
    owner_name: Optional[str] = None
    likes_count: Optional[int] = None
    liked_by_user: Optional[bool] = None


class CommentResponseModel(BaseModel):
    id: Optional[int] = None
    pet_id: Optional[int] = None
    date: Optional[str] = None
    message: Optional[str] = None
    user_id: Optional[int] = None
    user_name: Optional[str] = None


class GetResponseModel(BaseModel):
    pet: PetResponseModel
    comments: Optional[list[CommentResponseModel]] = None



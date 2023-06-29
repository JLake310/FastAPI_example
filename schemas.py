from typing import List, Union

from pydantic import BaseModel


# pydantic 라이브러리의 BaseModel 클래스를 상속 받아 ItemBase 생성 -> ":"를 사용하여 속성을 정의
class ItemBase(BaseModel):
    title: str
    description: Union[str, None] = None


class ItemCreate(ItemBase):
    pass


# API에서 데이터를 읽을 때/반환할 때 사용될 모델
class Item(ItemBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True


# UserBase 생성
class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool
    items: List[Item] = []

    class Config:
        orm_mode = True

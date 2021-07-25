from pydantic import BaseModel
from pydantic import UUID4
from typing import List

from .base import BaseSchema


class User(BaseModel):
    id: UUID4
    email: str
    token: str


class UserSchema(BaseSchema):
    data: List[User] = []

    class Config:
        orm_mode = True

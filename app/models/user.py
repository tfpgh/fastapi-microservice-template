import uuid

from pydantic import BaseModel, Field


class UserBase(BaseModel):
    name: str
    email: str  # This could be a pydantic EmailStr if email-validator was installed


class UserDB(UserBase):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))


class UserIn(UserBase):
    pass

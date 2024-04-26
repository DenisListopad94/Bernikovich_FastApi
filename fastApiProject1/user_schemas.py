from datetime import datetime
from enum import Enum
from typing import Optional

from pydantic import BaseModel


class UserRole(str, Enum):
    # Ваше перечисление ролей
    pass


class UserBaseSchema(BaseModel):
    first_name: str
    last_name: str
    role: UserRole
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None


class UserCreateSchema(UserBaseSchema):
    pass


class UserUpdatePartialSchema(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    role: Optional[UserRole] = None


class UserUpdateSchema(BaseModel):
    first_name: str
    last_name: str
    role: UserRole


class UserCreateRetrieveSchema(UserBaseSchema):
    id: int

    class Config:
        # Включим автоматическое создание атрибутов модели
        orm_mode = True

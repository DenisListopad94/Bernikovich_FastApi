
import sqlalchemy
from models import User
from sqlalchemy.orm import Session

from user_schemas import UserCreateSchema, UserUpdateSchema
from typing import Union

def create_user(
        user_schema: UserCreateSchema,
        session: Session,
) -> User:
    user = User()
    session.add(user)
    session.commit()

    return user


def get_users(
        session: Session
) -> list[User]:
    query = sqlalchemy.select(User)
    result = session.execute(query)
    data = result.scalars().all()

    return list(data)


def get_user_by_id(user_id: int, session: Session) -> User | None:
    return session.query(User).filter(User.id == user_id).first()


def update_user(
        session: Session,
        user: User,
        user_schema: UserUpdateSchema
) -> User:
    for name, value in user_schema.dict().items():
        setattr(user, name, value)
    session.commit()
    return user


def delete_user(
        session: Session,
        user: User,
) -> None:
    session.delete(user)
    session.commit()

def patch_user(
        session: Session,
        user: User,
        user_patch_schema: Union[UserUpdateSchema, dict]
) -> User:
    if isinstance(user_patch_schema, dict):
        user_patch_schema = UserUpdateSchema(**user_patch_schema)

    for field, value in user_patch_schema.dict(exclude_unset=True).items():
        setattr(user, field, value)
    session.commit()
    return user
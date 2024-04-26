from fastapi import APIRouter, status, Depends

from ..models import User
from ..schemas.user_schema import (
    UserSchema,
    UserCreateSchema,
    UserUpdateSchema,
    UserUpdatePartialSchema,
)

from ..services.user_service import (
    get_users,
    create_user,
    update_user,
    delete_user,
)
from ..utils.user_utils import get_user_info_by_id

@router.post("", response_model=UserCreateSchema, status_code=status.HTTP_201_CREATED)

def create_user_handler(
        user_schema: UserCreateSchema,
) -> User:
    user = create_user(
        user_schema =user_schema,
    )
    return user


@router.get("", response_model= list[UserSchema])
def get_users_handler():
    data = get_users()
    return data


@router.get("/{user_id}", response_model=UserSchema)
def get_user_handler(
        user=Depends(get_user_info_by_id),
) -> User:
    return user


@router.put("/{user_id}", response_model=UserUpdateSchema)
def update_user_handler(
        user_object: UserUpdateSchema,
) -> User:
    return update_user(
        user_schema=user_schema,
    )

@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user_handler(
        user=Depends(get_user_info_by_id),
) -> None:
   delete_user(

        user=user
    )


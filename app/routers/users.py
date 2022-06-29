from fastapi import APIRouter, Depends, HTTPException

from app.dependencies import CommonParameters, common_parameters
from app.models.user import UserDB, UserIn

router = APIRouter()


@router.get("/{user_id}", response_model=UserDB)
def get_user(
    user_id: str, commons: CommonParameters = Depends(common_parameters)
) -> UserDB:
    user = commons.user_store.get_user_by_id(user_id)
    if not user:
        raise HTTPException(404, "User with the given ID could not be found")

    return user


@router.post("/", response_model=UserDB, status_code=201)
def register_user(
    user: UserIn, commons: CommonParameters = Depends(common_parameters)
) -> UserDB:
    user_db = UserDB(**user.dict())
    commons.user_store.add_user(user_db)

    return user_db

from fastapi import APIRouter, HTTPException, Depends

from typing import Annotated

from schemas import UserData
from repositories import UsersRepository
from core import id_range, Converter


router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


@router.post("/new")
async def new_user(user: Annotated[UserData, Depends()]):
    created_user = await UsersRepository.add_user(UserData(**user.model_dump()))

    return {
        "status": 200,
        "user": created_user
    }


@router.get("/{id}")
async def get_user(id: id_range):
    if (user := await UsersRepository.get_user_by_id(id)) is not None:
        return {
            "status": 200,
            "user": Converter.convert_to_user_scheme(user)
        }
    
    else:
        raise HTTPException(status_code=404, detail="User not found.")

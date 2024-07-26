from fastapi import APIRouter

from schemas import UserScheme
from models import UserModel

from database import DataBase


router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


@router.post("/new")
async def new_user(user: UserScheme):
    await DataBase.add_user(UserModel(**user.model_dump()))

    return {
        "status": 200,
        "user": user
    }


from fastapi import APIRouter, HTTPException, Depends

from typing import Annotated

from schemas import UserData
from repositories import UsersRepository
from core.reused_types import pydantic_types 


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


@router.post("/edit")
async def edit_user(id: pydantic_types.id_range, data: Annotated[UserData, Depends()]):
    result = await UsersRepository.update_user_data(id, data)

    return {
        "status": 200,
        "data": result
    }


@router.delete("/delete")
async def delete_user(id: pydantic_types.id_range):
    result = await UsersRepository.remove_user_by_id(id)

    return {
        "status": 200,
        "removed": result
    }


@router.get("/search")
async def search_user(query: str):
    found = await UsersRepository.search_user(query)

    return {
        "status": 200,
        "total": len(found),
        "found": found
    }


@router.get("/{id}")
async def get_user(id: pydantic_types.id_range):
    if (user := await UsersRepository.get_user_by_id_as_scheme(id)) is not None:
        return {
            "status": 200,
            "user": user
        }
    
    else:
        raise HTTPException(status_code=404, detail="User not found.")

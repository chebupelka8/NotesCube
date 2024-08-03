from database import DataBase
from fastapi import HTTPException

from typing import Optional, Union, NoReturn
from sqlalchemy import select, or_

from models import UserModel
from schemas import UserData, UserScheme

from core import Converter, require_return_else_HTTPException
from core.reused_types import pydantic_types


class UsersRepository(DataBase):
 
    @classmethod
    async def add_user(cls, user: UserData) -> UserScheme:
        result = await cls.add_something_orm(UserModel, **user.model_dump())
        return UserScheme(**result)
    
    @classmethod
    @require_return_else_HTTPException("User not found.")
    async def remove_user_by_id(cls, user_id: pydantic_types.id_range) -> Union[NoReturn, UserScheme]:  # type: ignore
        if (target := await cls.get_by_id(UserModel, user_id)) is not None:
            result = await cls.remove_something_orm(target)
            return UserScheme(**result)
     
    @classmethod
    @require_return_else_HTTPException("User not found.")
    async def get_user_by_id_as_scheme(cls, user_id: pydantic_types.id_range) -> Union[NoReturn, UserScheme]:  # type: ignore
        if (returing := await cls.get_by_id_as_scheme(UserModel, user_id, UserScheme)) is not None:
            return returing
     
    @classmethod
    async def update_user_data(cls, user_id: int, data: UserData) -> UserScheme:
        async with cls.session() as session:
            async with session.begin():
                if (user := await session.get(UserModel, user_id)) is None:
                    raise HTTPException(status_code=404, detail="User not found.")

                user.first_name = data.first_name
                user.last_name = data.last_name

                updated = user.dump()
 
        return UserScheme(**updated)
    
    @classmethod
    async def search_user(cls, query: str) -> list[UserScheme]:
        async with cls.session() as session:
            statement = (
                select(UserModel)
                    .where(or_(
                        UserModel.first_name.contains(query),
                        UserModel.last_name.contains(query)
                    ))
                    .order_by(UserModel.id)
            )

            result = await session.execute(statement)

            return list(
                map(
                    Converter.convert_from_orm_model_to_scheme, result.scalars().all()
                )
            )

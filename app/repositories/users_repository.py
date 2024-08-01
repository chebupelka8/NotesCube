from database import AbstractDataBase
from fastapi import HTTPException

from typing import Optional
from sqlalchemy import select, or_

from models import UserModel
from schemas import UserData, UserScheme

from core import Converter
from core.reused_types import pydantic_types


class UsersRepository(AbstractDataBase):

    @classmethod
    async def add_user(cls, user: UserData) -> UserScheme:
        async with cls.session() as session:
            async with session.begin():
                new_user = UserModel(**user.model_dump())
                session.add(new_user)

                await session.flush()
                added = new_user.dump()
        
        return Converter.convert_from_orm_model_dump_to_scheme(added)
    
    @classmethod
    async def get_user_by_id(cls, user_id: pydantic_types.id_range) -> Optional[UserModel]:
        """returns detached user (cannot update using orm)"""

        async with cls.session() as session:
            result = await session.get(UserModel, user_id)
        
        return result
    
    @classmethod
    async def get_user_by_id_as_scheme(cls, user_id: pydantic_types.id_range) -> Optional[UserScheme]:
        if (user := await cls.get_user_by_id(user_id)) is not None:
            return Converter.convert_from_orm_model_to_scheme(user)
    
    @classmethod
    async def remove_user_by_id(cls, user_id: pydantic_types.id_range) -> UserScheme:
        async with cls.session() as session:
            async with session.begin():
                if (user := await cls.get_user_by_id(user_id)) is None:
                    raise HTTPException(status_code=404, detail="User not found.")
        
                await session.delete(user)
        
        return Converter.convert_from_orm_model_to_scheme(user) 
    
    @classmethod
    async def update_user_data(cls, user_id: int, data: UserData) -> UserScheme:
        async with cls.session() as session:
            async with session.begin():
                if (user := await session.get(UserModel, user_id)) is None:
                    raise HTTPException(status_code=404, detail="User not found.")

                user.first_name = data.first_name
                user.last_name = data.last_name

                updated = user.dump()
 
        return Converter.convert_from_orm_model_dump_to_scheme(updated)
    
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

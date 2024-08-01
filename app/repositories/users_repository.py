from database import AbstractDataBase
from fastapi import HTTPException

from typing import Optional
from sqlalchemy import select, or_

from models import UserModel
from schemas import UserData, UserScheme

from core import id_range, Converter


class UsersRepository(AbstractDataBase):

    @classmethod
    async def add_user(cls, user: UserData) -> UserScheme:
        async with cls.session() as session:
            async with session.begin():
                new_user = UserModel(**user.model_dump())
                session.add(new_user)

                await session.flush()
                added_user_id = new_user.id
        
        return UserScheme(id=added_user_id, **user.model_dump())
    
    @classmethod
    async def get_user_by_id(cls, user_id: id_range) -> Optional[UserModel]:
        """returns detached user (cannot update using orm)"""

        async with cls.session() as session:
            result = await session.get(UserModel, user_id)
        
        return result
    
    @classmethod
    async def remove_user_by_id(cls, user_id: id_range) -> UserScheme:
        async with cls.session() as session:
            async with session.begin():
                if (user := await cls.get_user_by_id(user_id)) is None:
                    raise HTTPException(status_code=404, detail="User not found.")
        
                await session.delete(user)
        
        return Converter.convert_to_user_scheme(user) 
    
    @classmethod
    async def update_user_data(cls, user_id: int, data: UserData) -> UserScheme:
        async with cls.session() as session:
            async with session.begin():
                if (user := await session.get(UserModel, user_id)) is None:
                    raise HTTPException(status_code=404, detail="User not found.")

                user.first_name = data.first_name
                user.last_name = data.last_name
        
        return Converter.convert_to_user_scheme(user)
    
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
                    Converter.convert_to_user_scheme, result.scalars().all()
                )
            )

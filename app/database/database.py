from .abstract_database import AbstractDataBase

from typing import Annotated, Optional
from sqlalchemy import select

from models import UserModel
from schemas import CreateUser, UserScheme

from core import id_range


class DataBase(AbstractDataBase):

    @classmethod
    async def add_user(cls, user: CreateUser) -> UserScheme:
        async with cls.session() as session:
            async with session.begin():
                new_user = UserModel(**user.model_dump())
                session.add(new_user)

                await session.flush()
                print(new_user)
                added_user_id = new_user.id
        
        return UserScheme(id=added_user_id, **user.model_dump())
    
    @classmethod
    async def get_user_by_id(cls, user_id: id_range) -> Optional[UserModel]:
        async with cls.session() as session:
            result = await session.get(UserModel, user_id)
            print(result)
        
        return result
 
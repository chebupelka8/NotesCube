from database import AbstractDataBase

from typing import Annotated, Optional
from sqlalchemy import select, update

from models import UserModel
from schemas import UserData, UserScheme

from core import id_range


class UsersRepository(AbstractDataBase):

    @classmethod
    async def add_user(cls, user: UserData) -> UserScheme:
        async with cls.session() as session:
            async with session.begin():
                new_user = UserModel(**user.model_dump())
                session.add(new_user)

                print(new_user)
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
    
    @classmethod
    async def update_user_data(cls, user_id: int, data: UserData) -> UserScheme:
        async with cls.session() as session:
            async with session.begin():
                statement = (
                    update(UserModel)
                        .where(UserModel.id == user_id)
                        .values(**data.model_dump())
                )

                await session.execute(statement)
        
        return UserScheme(id=user_id, **data.model_dump())

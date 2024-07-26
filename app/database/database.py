from .abstract_database import AbstractDataBase

from models import UserModel


class DataBase(AbstractDataBase):

    @classmethod
    async def add_user(cls, user: UserModel) -> None:
        async with cls.session() as session:
            async with session.begin():
                session.add(user)

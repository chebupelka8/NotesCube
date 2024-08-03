from faker import Faker

from models import UserModel
from .database import DataBase


class FakeFillDB(DataBase):
    __faker = Faker()

    @classmethod
    async def add_fake_users(cls, __count: int) -> None:
        if __count <= 0: return
            
        async with cls.session() as session:
            async with session.begin():
                for _ in range(__count):
                    session.add(UserModel(
                        first_name=cls.__faker.first_name(), last_name=cls.__faker.last_name()
                    ))

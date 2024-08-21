from faker import Faker
import random

from models import UserModel, NoteModel
from .database import AbstractDataBase


class FakeFillDB(AbstractDataBase):
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
    
    @classmethod
    async def add_fake_notes(cls, __count: int) -> None:
        if __count <= 0: return

        async with cls.session() as session:
            async with session.begin():
                for ident in range(1, __count):
                    if random.randint(0, 1):
                        session.add(NoteModel(
                            user_id=ident, 
                            title=" ".join(cls.__faker.words(random.randint(1, 4))),
                            description=cls.__faker.text(250),
                            content=cls.__faker.text(1000)
                        ))

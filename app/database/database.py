from typing import Type, Optional
from pydantic import BaseModel

from .abstract_database import AbstractDataBase
from models import AbstractModel


class DataBase(AbstractDataBase):

    @classmethod
    async def get_by_id[T: AbstractModel](cls, class_smth: Type[T], id: int) -> Optional[T]:
        """returns detached instance"""

        async with cls.session() as session:
            returing = await session.get(class_smth, id)
        
        return returing
    
    @classmethod
    async def get_by_id_as_scheme[T: BaseModel](cls, class_smth: Type[AbstractModel], id: int, like: Type[T]) -> Optional[T]:
        async with cls.session() as session:
            if (instance := await session.get(class_smth, id)) is not None:
                return like(**instance.dump()) 
    
    @classmethod
    async def add_something_orm(cls, class_smth: Type[AbstractModel], **kwargs) -> dict:
        async with cls.session() as session:
            async with session.begin():
                new_smth_model = class_smth(**kwargs)
                session.add(new_smth_model)

                await session.flush()
                returning = new_smth_model.dump()
        
        return returning
    
    @classmethod
    async def remove_something_orm(cls, instance_smth: AbstractModel) -> dict:
        async with cls.session() as session:
            async with session.begin():
                # if inspect(instance_smth).detached:
                #     raise HTTPException(status_code=500, detail="Detached instance orm.")
                
                await session.delete(instance_smth)
                returing = instance_smth.dump()
        
        return returing

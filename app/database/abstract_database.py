from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy import inspect

from typing import Type, Optional

from fastapi import HTTPException
from pydantic import BaseModel

from models import AbstractModel
from core import DATABASE_URL


class AbstractDataBase:
    engine = create_async_engine(DATABASE_URL, echo=True) # type: ignore
    session = async_sessionmaker(engine)

    @classmethod
    async def run_metadata_method(cls, method: str) -> None:
        if not hasattr(AbstractModel.metadata, method):
            raise HTTPException(status_code=500, detail=f"Method '{method}' not found.")

        async with cls.engine.connect() as connection:
            await connection.run_sync(
                getattr(AbstractModel.metadata, method)
            )
            
    @classmethod
    async def create_all_tables(cls) -> None:
        await cls.run_metadata_method("create_all")

    @classmethod
    async def drop_all_tables(cls) -> None:
        await cls.run_metadata_method("drop_all")
    
    @classmethod
    async def get_by_id(cls, class_smth: Type[AbstractModel], id: int) -> Optional[AbstractModel]:
        """returns detached instance"""

        async with cls.session() as session:
            returing = await session.get(class_smth, id)
        
        return returing
    
    @classmethod
    async def get_by_id_as_scheme(cls, class_smth: Type[AbstractModel], id: int, like: Type[BaseModel]) -> BaseModel:
        async with cls.session() as session:
            if (instance := await session.get(class_smth, id)) is not None:
                returing = like(**instance.dump())
            
            return returing
    
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

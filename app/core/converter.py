from typing import TYPE_CHECKING

import models, schemas
from pydantic import BaseModel

if TYPE_CHECKING:
    from schemas import UserScheme
    from models import UserModel


class Converter:

    @staticmethod
    def convert_from_orm_model_dump_to_scheme(orm_model_dump: dict) -> "UserScheme":
        return schemas.UserScheme(**orm_model_dump)
    
    @staticmethod
    def convert_from_orm_model_to_scheme(orm_model: "UserModel") -> "UserScheme":
        return Converter.convert_from_orm_model_dump_to_scheme(
            orm_model.dump()
        )
    
    @staticmethod
    def convert_from_scheme_to_orm_model(scheme: "UserScheme") -> "UserModel":
        return models.UserModel(
            **scheme.model_dump()
        )

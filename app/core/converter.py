from typing import TYPE_CHECKING

import models, schemas

if TYPE_CHECKING:
    from schemas import UserScheme
    from models import UserModel


class Converter:

    @staticmethod
    def convert_user_to_model(user_scheme: "UserScheme") -> "UserModel":
        return models.UserModel(
            **user_scheme.model_dump()
        ) 

    @staticmethod
    def convert_to_user_scheme(user_model: "UserModel") -> "UserScheme":
        return schemas.UserScheme(
            id=user_model.id,
            first_name=user_model.first_name,
            last_name=user_model.last_name
        )

from typing import Optional, TYPE_CHECKING

from sqlalchemy.orm import Mapped
from .abstract import AbstractModel

from core.reused_types import sqlalchemy_types


class UserModel(AbstractModel):
    __tablename__ = "users"

    first_name: Mapped[sqlalchemy_types.string64]
    last_name: Mapped[Optional[sqlalchemy_types.string64]] 
    created_at: Mapped[sqlalchemy_types.utc_creation_date] 
    updated_at: Mapped[sqlalchemy_types.utc_updated_date]

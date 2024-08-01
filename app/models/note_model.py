from typing import Optional, Annotated

from sqlalchemy import ForeignKey
from sqlalchemy.orm import mapped_column, Mapped

from .abstract import AbstractModel
from core.reused_types import sqlalchemy_types


class NoteModel(AbstractModel):
    __tablename__ = "notes"

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    title: Mapped[sqlalchemy_types.string64]
    description: Mapped[Optional[sqlalchemy_types.string256]]
    content: Mapped[Optional[str]]
    created_at: Mapped[sqlalchemy_types.utc_creation_date] 
    updated_at: Mapped[sqlalchemy_types.utc_updated_date]

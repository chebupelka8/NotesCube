from sqlalchemy import String
from sqlalchemy.orm import mapped_column

from datetime import datetime
from typing import Annotated

from pydantic import Field


type string256 = Annotated[str, mapped_column(String(256))]
type string64 = Annotated[str, mapped_column(String(64))]

type utc_creation_date = Annotated[
    datetime, mapped_column(default=datetime.utcnow)
]

type utc_updated_date = Annotated[
    datetime, mapped_column(onupdate=datetime.utcnow, default=datetime.utcnow)
]

type id_range = Annotated[int, Field(gt=0)]

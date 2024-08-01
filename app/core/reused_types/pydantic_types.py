from pydantic import Field
from typing import Annotated


type id_range = Annotated[int, Field(gt=0)]
type string256 = Annotated[str, Field(max_length=256)]
type string64 = Annotated[str, Field(max_length=64)]

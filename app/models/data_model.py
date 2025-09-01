from pydantic import BaseModel
from typing import List

class Item(BaseModel):
    name: str
    value: float

class DataBatch(BaseModel):
    items: List[Item]

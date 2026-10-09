from pydantic import BaseModel
from typing import Optional

class BookCreate(BaseModel):
    bh:str
    bname:str
    price:str


class BookUpdate(BaseModel):
    bh:str |None=None
    bname:str|None=None
    price:str|None=None


class BookRead(BaseModel):
    id:int
    bh:str
    bname:str
    price:str
    model_config={"from_attributes":True}
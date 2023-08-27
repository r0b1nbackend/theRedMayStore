from pydantic import BaseModel
from typing import Optional,List


class Book(BaseModel):
    book:str
    author:str
    description:str
    price:int
    isHave:bool

    class Config:
        schema_extra = {
            "book":"Balada of Edichka",
            "author":"Eduard Limonov",
            "description":"Life of Eduard Limonov",
            "price":1890,
            "isHave":True
        }
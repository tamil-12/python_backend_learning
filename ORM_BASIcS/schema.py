from pydantic import BaseModel
from typing import Optional


class BookBase(BaseModel):
    title: str
    desc: str
    year: int


class BookCreate(BookBase):
    pass


class BookUpdate(BaseModel):
    title: Optional[str]
    desc: Optional[str]
    year: Optional[int]


class BookResponse(BookBase):
    id: int

    class Config:
        orm_mode = True

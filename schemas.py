from pydantic import BaseModel, validator, Field
from datetime import date
from typing import List


class Genre(BaseModel):
    name: str


class Author(BaseModel):
    first_name: str = Field(
        ...,
        max_length=55,
    )
    last_name: str
    age: int = Field(
        ...,
        gt=18,
        lt=110,
        description='Author age must be greater than 18 and less than 110.',
    )


class Book(BaseModel):
    title: str
    writer: str
    duration: str
    date: date
    summary: str
    genres: List[Genre] = []
    pages: int


class BookOut(Book):
    id: int

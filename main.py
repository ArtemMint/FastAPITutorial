from typing import List
from fastapi import FastAPI, Query, Path, Body

from schemas import *

app = FastAPI()


@app.post('/author/')
def create_author(author: Author = Body(...,
                                        embed=True)):
    return {
        'author': author,
    }


@app.post('/book', response_model=BookOut)
def create_book(item: Book = Body(...,
                                  embed=True,)):
    return BookOut(**item.dict(), id=44)


@app.get('/book/')
def get_book(q: List[str] = Query(['book1', 'book2'],
                                  description='Search book'),):
    return q


@app.get('/book/{pk}/')
def get_single_book(
        pk: int = Path(..., gt=1, le=25,),
        pages: int = Query(None, gt=10, le=500), ):
    return {
        'pk': pk,
        'pages': pages,
    }

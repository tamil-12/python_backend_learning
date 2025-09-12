from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()


class Book(BaseModel):
    id: int
    title: str
    description: str
    year: int


class BookUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    year: Optional[int] = None


book_db: List[Book] = []


@app.get("/books", status_code=200)
def get_books():
    """Return list of all books"""
    return book_db


@app.post("/books", status_code=201)
def add_book(book: Book):
    """Create a new book entry in list"""
    for b in book_db:
        if b.id == book.id:
            raise HTTPException(
                status_code=400, detail="Book with given ID already exists"
            )
    book_db.append(book)
    return {"message": "New book added successfully"}


@app.put("/books/{book_id}", status_code=200)
def update_books(book_id: int, updated_book: Book):
    """Update book details based on book id"""
    for index, b in enumerate(book_db):
        if b.id == book_id:
            book_db[index] = updated_book
            return {"message": "Book updated successfully"}
    raise HTTPException(status_code=404, detail="Book with given ID not found")


@app.patch("/books/{book_id}", status_code=200)
def patch_book(book_id: int, updated_book: BookUpdate):
    """Update on particular data in book db"""
    for index, b in enumerate(book_db):
        if b.id == book_id:
            if updated_book.title is not None:
                book_db[index].title = updated_book.title
            if updated_book.description is not None:
                book_db[index].description = updated_book.description
            if updated_book.year is not None:
                book_db[index].year = updated_book.year
            return {"message": "Book updated successfully"}
    raise HTTPException(status_code=404, detail="Book not found")


@app.delete("/books/{book_id}", status_code=200)
def delete_book(book_id: int):
    """Delete book using its id"""
    for b in book_db:
        if b.id == book_id:
            book_db.remove(b)
            return {"message": "Book deleted successfully"}
    raise HTTPException(status_code=404, detail="Book with given ID not found")

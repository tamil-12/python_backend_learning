from fastapi import HTTPException
from sqlalchemy.orm import Session
from models import Book
from schema import BookCreate, BookUpdate


def get_books(db: Session):
    return db.query(Book).all()


def get_book(db: Session, book_id: int):
    book = db.query(Book).filter(Book.id == book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book


def create_book(db: Session, book: BookCreate):
    db_book = Book(**book.dict())
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book


def update_book(db: Session, book_id: int, book: BookUpdate):
    db_book = db.query(Book).filter(Book.id == book_id).first()
    if db_book:
        for key, value in book.dict(exclude_unset=True).items():
            setattr(db_book, key, value)
        db.commit()
        db.refresh(db_book)
        return db_book
    raise HTTPException(status_code=404, detail="Book not found")


def delete_book(db: Session, book_id: int):
    book = get_book(db, book_id)
    db.delete(book)
    db.commit()
    return {"detail": "Book deleted"}

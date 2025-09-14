from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
import crud, schema
from database import get_db
from auth import require_role

router = APIRouter(prefix="/books", tags=["books"])


@router.get("/", response_model=list[schema.BookResponse])
def read_books(db: Session = Depends(get_db)):
    return crud.get_books(db)


@router.get("/{book_id}", response_model=schema.BookResponse)
def read_book(book_id: int, db: Session = Depends(get_db)):
    return crud.get_book(db, book_id)


@router.post(
    "/",
    response_model=schema.BookResponse,
    status_code=status.HTTP_201_CREATED,
    dependencies=[Depends(require_role("admin"))],
)
def create_book(book: schema.BookCreate, db: Session = Depends(get_db)):
    return crud.create_book(db, book)


@router.put("/{book_id}", response_model=schema.BookResponse)
def update_book(book_id: int, 
                book: schema.BookUpdate, 
                db: Session = Depends(get_db)):
    return crud.update_book(db, book_id, book)


@router.delete("/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_book(book_id: int, db: Session = Depends(get_db)):
    return crud.delete_book(db, book_id)

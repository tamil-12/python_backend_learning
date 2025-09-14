from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from crud import get_user, create_user, verify_password
from schema import UserCreate, UserResponse
from database import get_db
from auth import create_access_token


router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/register", response_model=UserResponse)
def register(user: UserCreate, db: Session = Depends(get_db)):
    if get_user(db, user.username):
        raise HTTPException(status_code=400, detail="Username already registered")
    return create_user(db, user)


@router.post("/token")
def login(username: str, password: str, db: Session = Depends(get_db)):
    user = get_user(db, username)
    if not user or not verify_password(password, user.hashed_password):
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    access_token = create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}

from fastapi import FastAPI
from database import engine, Base
from routes import book

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Book store API", version=1.0)

app.include_router(book.router)


@app.get("/")
def initial_route():
    return {"message": "Welcome to Bookstore API"}

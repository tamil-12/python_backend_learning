from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def initial_route():
    return "Welcome to home page"
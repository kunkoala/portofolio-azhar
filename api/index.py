# API
from fastapi import FastAPI

app = FastAPI()

@app.get("/api/hello")
def read_root():
    return {"message": "Hello World! This API is now working yippie!"}

@app.get("/")
def home():
    return {"message": "Welcome to the site!"}
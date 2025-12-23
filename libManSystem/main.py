from fastapi import FastAPI
from model import create_table
from router import student, book

app = FastAPI(tittle="Library Managment System")

create_table()

app.include_router(student.router)
app.include_router(book.router)

@app.get("/")
def home():
    return{"message":"Library API running"}

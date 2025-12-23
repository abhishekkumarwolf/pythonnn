from pydantic import BaseModel

class StudentCreate(BaseModel):
    stdID: int
    name: str
    contact: str
    branch: str
    year: str

class BookCreate(BaseModel):

    bookId: int
    bname: str
    author: str


class BookAction(BaseModel):
    stdID: int
    name:str
    author:str


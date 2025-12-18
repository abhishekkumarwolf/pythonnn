from pydantic import BaseModel
from typing import List

class StudentCreate(BaseModel):
    stdId: int
    name :str
    marks: List[str]

class StudentResponse(StudentCreate):
    total :int
    average: float
    grades : List[str]

    class Config:
        from_attributres = True

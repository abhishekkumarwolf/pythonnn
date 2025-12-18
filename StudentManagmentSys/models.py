from sqlalchemy import Column, Integer, String, JSON
from database import Base

class StudentModel(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    mark = Column(JSON)

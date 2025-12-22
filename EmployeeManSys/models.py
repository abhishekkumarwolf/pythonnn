from sqlalchemy import Column, Integer, String
from database import Base 


class Employee(Base):

    __tablename__="employees"

    empId = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    degree = Column(String)
    department = Column(String)
    base_salary = Column(Integer)

    

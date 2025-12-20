from pydantic import BaseModel

class EmployeeCreate(BaseModel):

    empId: int
    name: str
    degree: str
    department: str
    base_salary: int


class EmployeeResponse(EmployeeCreate):
    final_salary: float

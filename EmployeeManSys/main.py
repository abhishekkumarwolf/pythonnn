from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from database import SessionLocal , engine
from models import Employee
from schemas import EmployeeCreate, EmployeeResponse

app = FastAPI(tittle="Employee Managment API")

from models import Base
Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def calculate_salary(base_salary: int, role:str):
    if role == "Engineer":
        return base_salary + base_salary*0.3
    elif role == "Manager":
        return base_salary + base_salary*0.6
    return base_salary


@app.post("/employees", response_model=EmployeeResponse)
def register_employee(emp: EmployeeCreate, db: Session = Depends(get_db)):
    existing = db.query(Employee).filter(Employee.empId == emp.empId).first()
    if existing:
        raise HTTPException(status_code=400, details=" Employee already exists")
    
    employee = Employee(
        empId = emp.empId,
        name=emp.name,
        base_salary=emp.base_salary,
        degree = emp.degree,
        department= emp.department
    )

    db.add(employee)
    db.commit()
    db.refresh(employee)

    final_salary = calculate_salary(emp.base, emp.department)

    return{
        **emp.dict(),
        "final_salary": final_salary
    }


@app.get("/employees/{empId}", response_model=EmployeeResponse)
def login_employee(
    empId: int,
    db: Session = Depends(get_db)
):
    employee = db.query(Employee).filter(Employee.empId == empId).first()

    if not employee:
        raise HTTPException(status_code=400, details="Employee not found")
    
    final_salary = calculate_salary(employee.base_salary, employee.department)

    return{
        "empId" : employee.empId,
        "name" : employee.name,
        "base_salary": employee.base_salary,
        "degree":employee.degree,
        "department":employee.department,
        "final_salary": final_salary
    }


@app.post("/attendence/{empId}")
def submit_attendence(empId: int, db:Session = Depends(get_db)):

    employee = db.query(Employee).filter(Employee.empId == empId).first()

    if not employee:
        raise HTTPException(status_code=400, details=" Employee not found")
    
    return {"message": "Attendence submitted succesfully"}
    
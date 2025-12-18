from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import models, database, schemas


models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

def get_db():
    db = database.sessionlocal()
    try:
        yield db
    finally:
        db.close()


def calculate_grades(marks: list[int]):
    results = []
    for m in marks:
        if m >90: grade = "A"
        elif m >80: grade ="B"
        elif m > 70: grade ="C"
        elif m > 60: grade = "D"
        else : grade = "Failed"
        results.append(f"mark {m} : {grade}")
    return results

@app.post("/register", response_model=schemas.StudentResponse)
def register_student(student: schemas.StudentCreate, db : Session = Depends(get_db)):
    db_student = db.query(models.StudentDB).filter(models.StudentDB.stdID == student.stdId).first()
    if db_student:
        raise HTTPException(status_code=404, details="Student ID already exists")
    
    new_student = models.StudentDB(
        stdId=student.stdId,
        name = student.name,
        marks = student.marks

    )

    db.add(new_student)
    db.commit()
    db.refresh(new_student)

    total_val = sum(new_student.marks)
    return {
        **student.dict(),
        "total": total_val,
        "Average ": total_val / len(new_student.marks),
        "grades": calculate_grades(new_student.marks)
    }

@app.get("/report/{stdId}", response_model=schemas.StudentResponse)
def get_report(stdId : int, db: Session = Depends(get_db)):
    student = db.query(models.StudentDB).filter(models.StudentDB.stdId == stdId).first()
    if not student:
        raise HTTPException(status_code=404, details="Student not found")
    
    total_val = sum(student.marks)
    return{
        "stdId" : student.stdId,
        "name" : student.name,
        "marks": student.marks,
        "Total": total_val,
        "Average": total_val/len(student.marks),
        "grades": calculate_grades(student.marks)
    }










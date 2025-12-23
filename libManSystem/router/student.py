from fastapi import APIRouter, HTTPException
from database import get_connection
from schemas import StudentCreate

router = APIRouter(prefix="/students", tags=["Students"])

@router.post("/register")
def register_student(student: StudentCreate):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM students WHERE stdId=?",(student.stdId))
    if cur.fetchone():
        raise HTTPException(status_code=404, details="Student already exist")
    
    cur.execute(
        "INSERT INTO students VALUES (?,?,?,?)",
        (student.stdId, student.name, student.contact,student.branch, student.year)
    )

    conn.commit()
    conn.close()
    return {"message": "Student registerd successfully"}


@router.get("/login/{stdId}")
def login(stdId: int):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM students WHERE stdId=?", (stdId,))
    student = cur.fetchone()
    conn.close()

    if not student:
        raise HTTPException(status_code=404, details="Studen not found")
    
    return dict(student)

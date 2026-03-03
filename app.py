from fastapi import FastAPI, Path
from pydantic import BaseModel
app = FastAPI()

#GET - get or return info
#POST - Create something new
#PUT - update data
#DELETE

students = {
    1: {
        "name": "Arnav",
        "age": 18,
        "sem": "VI"
    }
}
class Student(BaseModel):
    name : str
    age: int
    sem: str
@app.get("/")
def index():
    return {"name": "Hello"}

@app.get("/get-student/{student_id}")
def get_student(student_id : int = Path(description="Enter Student ID", gt = 0)): # gt, ls , ge (greater than)
    return students[student_id]

@app.get("/get-by-name")
def get_student(name: str):
    for student_id in students:
        if students[student_id]["name"] == name:
            return students[student_id]
        return "Data not Found !!"

@app.post("/create-student/{student_id}")
def create_student(student_id: int , student: Student):
    if student_id in students:
        return "Student exists"
    students[student_id] = student.model_dump()
    return students[student_id]

@app.put("/update-student/{student_id}")
def update_student():
    pass
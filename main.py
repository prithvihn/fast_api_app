from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()
class student(BaseModel):
    id: int
    name: str
    age: int
    roll_number: int
    department: str
class Studentresponse(BaseModel):
    id: int
    name: str
    age: int
    roll_number: int
    department: str
@app.get("/")
def read_root():
    return {"Hello": "World"}
    

@app.post("/students/", response_model=Studentresponse)
def create_student(student: student):
    return Studentresponse(id=1, name=student.name, age=student.age, roll_number=student.roll_number, department=student.department)

@app.get("/students/", response_model=List[Studentresponse])
def read_students() -> List[Studentresponse]:
    return [Studentresponse(id=1, name="John", age=20, roll_number=101, department="CS")]

@app.put("/students/{student_id}", response_model=Studentresponse)
def update_student(student_id: int, student: student):
    return Studentresponse(id=student_id, name=student.name, age=student.age, roll_number=student.roll_number, department=student.department)

@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    return {"message": f"Student with id {student_id} deleted successfully"}
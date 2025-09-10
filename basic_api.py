from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

students = {}


class Student(BaseModel):
    name: str
    age: int


class UpdateStudent(BaseModel):
    name: Optional[str]
    age: Optional[int]


class DeleteStudent(BaseModel):
    name: Optional[str]
    age: Optional[int]


@app.get("/")
def initial_route():
    """Simple return function of inital route"""
    return "Welcome to home page"


# Path parameter example
@app.get("/get-details/{student_id}")
def get_student_details(student_id: int):
    """Return student details based on student id"""
    return students[student_id]


# Query Parameter example
@app.get("/get-by-name")
def get_student_by_name(name: str):
    """Return student details based on student name"""
    for student_id in students:
        if students[student_id]["name"] == name:
            return students[
                student_id
            ]  # Return Student details if name matches in query parameter
        return "Data not found"


@app.post("/add-student/{student_id}")
def add_student(student_id: int, student: Student):
    """Add student details based on student id"""
    if student_id in students:
        return {"Error": "Student already exists"}
    students[student_id] = student.dict()
    return students[student_id]


@app.put("/update-student/{student_id}")
def update_student(student_id: int, student: UpdateStudent):
    """Update student particular data using studnet id"""
    if student_id not in students:
        return {"Error": "Student data not found"}
    if student.name:
        students[student_id]["name"] = student.name
    elif student.age:
        students[student_id]["age"] = student.age
    return students[student_id]


@app.delete("/delete-student/{student_id}")
def delete_student(student_id: int):
    """Delete student data using student id"""
    if student_id not in students:
        return {"Error": "Student data not found"}
    students.pop(student_id)
    return {"Message": "Student data deleted successfully"}

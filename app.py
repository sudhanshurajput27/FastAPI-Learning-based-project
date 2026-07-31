from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Student(BaseModel):
    name: str
    age:int

@app.post("/students")
def create_student(student: Student):
    return student










































'''from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Welcome"}


@app.get("/about")
def about():
    return{"message": "This our first API"}


@app.get("/students")
def create_student():
    return{
        "message": "Student Created"
    }


@app.get("/search")
def search_student(name: str, age: int):
    return {
        "name": name,
        "age": age
    }
'''

from fastapi import FastAPI
from pydantic import BaseModel
import joblib

app = FastAPI()

model = joblib.load("saved_model/model.pkl")

class IrisData(BaseModel):
    feature1: float
    feature2: float
    feature3: float
    feature4: float

@app.post("/predict")
def predict(data: IrisData):

    features = [[
        data.feature1,
        data.feature2,
        data.feature3,
        data.feature4
    ]]

    prediction = model.predict(features)

    return {
        "prediction": int(prediction[0])
    }









































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

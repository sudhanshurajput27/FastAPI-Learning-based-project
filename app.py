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

    flower_names = {
        0: "Setosa",
        1: "Versicolor",
        2: "Virginica"
    }

    features = [[
        data.feature1,
        data.feature2,
        data.feature3,
        data.feature4
    ]]

    prediction = model.predict(features)

    result = flower_names[prediction[0]]

    return {"prediction": result}
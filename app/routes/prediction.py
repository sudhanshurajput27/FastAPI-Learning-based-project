from fastapi import APIRouter

from app.schemas.iris_schema import IrisData
from app.services.prediction_service import make_prediction

router = APIRouter()

@router.post("/predict")
def predic(data: IrisData):

    result = make_prediction(data)

    return {
        "prediction": result
    }
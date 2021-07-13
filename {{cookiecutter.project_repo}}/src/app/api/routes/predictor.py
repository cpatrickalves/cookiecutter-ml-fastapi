from models.prediction import HealthResponse, PredictServiceInput, PredictServiceResponse
from services.predict import MachineLearningModelHandlerScore as model
from fastapi import APIRouter, HTTPException, status
from core.config import VERSION, PROJECT_NAME
from core.errors import PredictException
from loguru import logger
from typing import Any
import joblib
import json


router = APIRouter()

get_prediction = lambda data_input: PredictServiceResponse(
    model.predict(data_input, load_wrapper=joblib.load, method="predict_proba")
)


@router.get("/predict", input_data=PredictServiceInput,
            response_model=PredictServiceResponse,
            name="predict:get-data")
async def predict(data_input: Any = None):
    if not data_input:
        raise HTTPException(status_code=404, detail=f"'data_input' argument invalid!")
    try:
        prediction = get_prediction(data_input)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Exception: {e}")

    return PredictServiceResponse(prediction=prediction)
from pydantic import BaseModel
from typing import Optional


class PredictServiceInput(BaseModel):
    secret_key: str
    queuing: bool = True
    some_input: str = ""

    class Config:
        schema_extra = {
            "example": {
                "some_input": "somevalue",
                "secret_key": "SomeSecret"
            }
        }


class TrainServiceInput(BaseModel):
    secret_key: str
    dataset_id: str
    model_id: str

    class Config:
        schema_extra = {
            "example": {
                "dataset_id": "dataset_id",
                "model_id": "model_id",
                "secret_key": "SomeSecret"
            }
        }


class PredictServiceResponse(BaseModel):
    prediction: float


class HealthResponse(BaseModel):
    status: bool

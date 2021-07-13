from models.prediction import HealthResponse
from services.predict import MachineLearningModelHandlerScore as model
from fastapi import APIRouter, HTTPException, status
from core.config import VERSION, PROJECT_NAME
from loguru import logger
import json
import os


router = APIRouter()

@router.get(
    "/health", response_model=HealthResponse, name="health:get-data",
)
async def health():
    is_health = False
    try:
        # RUN PREDICT API
        is_health = True
        return HealthResponse(status=is_health)
    except Exception:
        raise HTTPException(status_code=404, detail="Unhealthy")


@router.get("/status")
def get_status():
    """
    Root view returns the system status
    """

    return {"api": PROJECT_NAME, "status": f"online", "version": VERSION}


@router.get("/models")
def get_models():
    """Return all models available
    """

    API_NAME = os.environ.get("API_NAME")
    MODEL_FOLDER = os.environ.get("MODEL_FOLDER")

    logger.info(f"{API_NAME} - receives a GET in /models")

    models_files = []
    models_data = []
    filename = "model.json"

    # Walking top-down from the root
    for root, dir, files in os.walk(str(MODEL_FOLDER)):
        if filename in files:
            print(root, dir, files)
            models_files.append(os.path.join(root, filename))

    n_models = len(models_files)
    message = f"Found {n_models} models: {str(models_files)}"
    logger.info(message)

    if n_models == 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="no models found")

    for model_file in models_files:
        with open(model_file, "r") as mfile:
            json_data = json.load(mfile)
            models_data.append({"model_id": json_data.get("model_id", None), "metadata": json_data})

    logger.info({"models": models_data})
    return {"models": models_data}

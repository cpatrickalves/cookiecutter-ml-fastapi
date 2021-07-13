from fastapi import APIRouter
from api.routes import trainer
from api.routes import common
from api.routes import predictor


router = APIRouter()
router.include_router(predictor.router, tags=["predictor"], prefix="/v1")
router.include_router(predictor.router, tags=["trainer"], prefix="/v1")
router.include_router(predictor.router, tags=["common"], prefix="/v1")

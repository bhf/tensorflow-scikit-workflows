from typing import List

from core.utils.logger import get_logger
from fastapi import APIRouter

from api.app.injector import get_sklearn_controller
from api.dto.RegressionResultDTO import RegressionResultDto

router = APIRouter()
logger = get_logger(__name__)

@router.get("/ols")
async def get_ols() -> RegressionResultDto:
    logger.info("Got call to ols endpoint")
    controller = get_sklearn_controller()
    return controller.get_ols_result()

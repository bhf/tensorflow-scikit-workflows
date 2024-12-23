from functools import lru_cache

from api.controller.sklearn_controller import SklearnController
from core.utils.logger import get_logger

logger = get_logger(__name__)


@lru_cache()
def get_sklearn_controller() -> SklearnController:
    logger.info("call get_sklearn_controller!")
    controller = SklearnController()
    return controller

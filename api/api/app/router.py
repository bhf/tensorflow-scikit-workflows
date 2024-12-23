from typing import List

from core.utils.logger import get_logger
from fastapi import APIRouter

from api.app.injector import get_user_controller
from api.dto.user import UserDto, CreateUserDto, UserCreateStatusDto, UsersDto

router = APIRouter()
logger = get_logger(__name__)

@router.get("/users")
async def get_all_users() -> UsersDto:
    logger.info("Got call to users endpoint")
    controller = get_user_controller()
    return controller.find_all_user()


@router.get("/users/{user_id}")
async def get_user_by_id(user_id: str) -> UserDto:
    logger.info("Got call to user "+ user_id)
    #controller = get_user_controller()
    #return controller.find_user_by_user_id(user_id)


@router.post("/users/create")
async def get_user_by_id(user: CreateUserDto) -> UserCreateStatusDto:
    controller = get_user_controller()
    return controller.create_user(user)

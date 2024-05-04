from fastapi import APIRouter

from src.api.route.user import router as user_router
from src.api.route.auth import router as auth_router
from src.api.route.new import router as new_router
from src.api.route.announcement import router as announcement_router


main_router = APIRouter(prefix="/api/v1")

main_router.include_router(router=auth_router)
main_router.include_router(router=user_router)
main_router.include_router(router=new_router)
main_router.include_router(router=announcement_router)

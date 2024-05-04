from fastapi import APIRouter

from src.api.route.user import router as user_router


main_router = APIRouter(prefix="/api/v1")

main_router.include_router(router=user_router)


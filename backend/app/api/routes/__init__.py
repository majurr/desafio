from app.api.routes.defaults import router as defaults_router
from app.api.routes.users import router as users_router
from fastapi import APIRouter

router = APIRouter()


router.include_router(users_router, prefix="/users", tags=["users"])
router.include_router(defaults_router, prefix="/defaults", tags=["defaults"])

from fastapi import APIRouter

from app.api.endpoints import common

api_router = APIRouter()

api_router.include_router(common.router, tags=["common"])

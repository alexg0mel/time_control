from fastapi import APIRouter

from app.api.endpoints import common, project, timeline

api_router = APIRouter()

api_router.include_router(common.router, tags=["common"])
api_router.include_router(project.router, tags=["project"])
api_router.include_router(timeline.router, tags=["timeline"])

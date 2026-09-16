from fastapi import APIRouter
from .auth import auth_router
Router = APIRouter()

Router.include_router(auth_router)
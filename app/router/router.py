from fastapi import APIRouter

from .auth import auth_router
from .search import search_router

Router = APIRouter()

Router.include_router(auth_router)
Router.include_router(search_router)
from fastapi import FastAPI
from app.router.router import Router
from app.db.base import create_tables

app = FastAPI()
create_tables()
app.include_router(Router)



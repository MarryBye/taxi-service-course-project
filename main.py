from fastapi import FastAPI
from src.routes.users import router as users_router

from src.database.controller import database

app = FastAPI()

app.include_router(users_router, tags=["Users"], prefix="/api",)
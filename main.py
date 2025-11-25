from fastapi import FastAPI
from src.routes.index import router

from src.database.controller import database

app = FastAPI()

app.include_router(router)
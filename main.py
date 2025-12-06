from fastapi import FastAPI
from src.routes.users import router as users_router
from src.routes.auth import router as auth_router
from src.routes.cars import router as cars_router

app = FastAPI()

app.include_router(users_router, tags=["Users"], prefix="/api",)
app.include_router(auth_router, tags=["Auth"], prefix="/api",)
app.include_router(cars_router, tags=["Cars"], prefix="/api",)
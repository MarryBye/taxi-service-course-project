from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.routes.auth import router as auth_router
from src.routes.admin import router as admin_router
from src.routes.worker import router as worker_router
from src.routes.authorized import router as authorized_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router, tags=["Auth"], prefix="/api")
app.include_router(admin_router, tags=["Admin"], prefix="/api")
app.include_router(worker_router, tags=["Worker"], prefix="/api")
app.include_router(authorized_router, tags=["Client"], prefix="/api")

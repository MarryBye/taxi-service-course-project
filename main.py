from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.sessions import SessionMiddleware
# from src.routes.users import router as users_router
from src.routes.auth import router as auth_router
# from src.routes.profile import router as profile_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_middleware(
    SessionMiddleware,
    secret_key="your-secret-key-here"
)

app.include_router(auth_router, tags=["Auth"], prefix="/api")

# app.include_router(profile_router, tags=["Profile"], prefix="/api")
#
# app.include_router(users_router, tags=["Users"], prefix="/api")
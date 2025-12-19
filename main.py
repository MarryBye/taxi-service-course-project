from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
# from src.routes.users import router as users_router
from src.routes.auth import router as auth_router
# from src.routes.cars import router as cars_router
# from src.routes.clients import router as clients_router
# from src.routes.maintenances import router as maintenances_router
# from src.routes.orders import router as orders_router
# from src.routes.drivers import router as drivers_router
# from src.routes.transactions import router as transactions_router

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
# app.include_router(users_router, tags=["Users"], prefix="/api")
# app.include_router(cars_router, tags=["Cars"], prefix="/api")
# app.include_router(clients_router, tags=["Clients"], prefix="/api")
# app.include_router(maintenances_router, tags=["Maintenances"], prefix="/api")
# app.include_router(orders_router, tags=["Orders"], prefix="/api")
# app.include_router(drivers_router, tags=["Drivers"], prefix="/api")
# app.include_router(transactions_router, tags=["Transactions"], prefix="/api")

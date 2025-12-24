from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse

from src.schemas.auth import TokenDataSchema
from src.schemas.views import *
from src.schemas.admin import *
from src.dependencies.has_role import require_roles
from src.services.admin import AdminService

router = APIRouter(prefix='/admin')

@router.post('/users')
async def create_user(data: CreateUserSchema, user: TokenDataSchema = Depends(require_roles('admin'))) -> UsersView:
    data = AdminService.create_user(data, user)

    if isinstance(data, Exception):
        raise HTTPException(400, str(data))

    return data

@router.get('/users')
async def users_list(user: TokenDataSchema = Depends(require_roles('admin'))) -> list[UsersView]:
    data = AdminService.get_users(user)

    if isinstance(data, Exception):
        raise HTTPException(400, str(data))

    return data

@router.get('/users/{user_id}')
async def user_info(user_id: int, user: TokenDataSchema = Depends(require_roles('admin'))) -> UsersView:
    data = AdminService.get_user(user_id, user)

    if isinstance(data, Exception):
        raise HTTPException(400, str(data))

    return data

@router.get('/users/{user_id}/stats/client')
async def client_stats(user_id: int, user: TokenDataSchema = Depends(require_roles('admin'))) -> ClientsStatView:
    data = AdminService.get_client_statistics(user_id, user)

    if isinstance(data, Exception):
        raise HTTPException(400, str(data))

    return data

@router.get('/users/{user_id}/stats/driver')
async def driver_stats(user_id: int, user: TokenDataSchema = Depends(require_roles('admin'))) -> DriversStatView:
    data = AdminService.get_driver_statistics(user_id, user)

    if isinstance(data, Exception):
        raise HTTPException(400, str(data))

    return data

@router.delete('/users/{user_id}')
async def delete_user(user_id: int, user: TokenDataSchema = Depends(require_roles('admin'))) -> None:
    data = AdminService.delete_user(user_id, user)

    if isinstance(data, Exception):
        raise HTTPException(400, str(data))

    return data

@router.put('/users/{user_id}')
async def update_user(user_id: int, data: UpdateUserSchema, user: TokenDataSchema = Depends(require_roles('admin'))) -> UsersView:
    data = AdminService.update_user(user_id, data, user)

    if isinstance(data, Exception):
        raise HTTPException(400, str(data))

    return data

@router.post('/cars')
async def create_car(data: CreateCarSchema, user: TokenDataSchema = Depends(require_roles('admin'))) -> CarsView:
    data = AdminService.create_car(data, user)

    if isinstance(data, Exception):
        raise HTTPException(400, str(data))

    return data

@router.get('/cars')
async def cars_list(user: TokenDataSchema = Depends(require_roles('admin'))) -> list[CarsView]:
    data = AdminService.get_cars(user)

    if isinstance(data, Exception):
        raise HTTPException(400, str(data))

    return data

@router.get('/cars/{car_id}')
async def car_info(car_id: int, user: TokenDataSchema = Depends(require_roles('admin'))) -> CarsView:
    data = AdminService.get_car(car_id, user)

    if isinstance(data, Exception):
        raise HTTPException(400, str(data))

    return data

@router.delete('/cars/{car_id}')
async def delete_car(car_id: int, user: TokenDataSchema = Depends(require_roles('admin'))) -> None:
    data = AdminService.delete_car(car_id, user)

    if isinstance(data, Exception):
        raise HTTPException(400, str(data))

    return data

@router.put('/cars/{car_id}')
async def update_car(car_id: int, data: UpdateCarSchema, user: TokenDataSchema = Depends(require_roles('admin'))) -> CarsView:
    data = AdminService.update_car(car_id, data, user)

    if isinstance(data, Exception):
        raise HTTPException(400, str(data))

    return data

@router.get('/orders')
async def orders_list(user: TokenDataSchema = Depends(require_roles('admin'))) -> list[OrdersView]:
    data = AdminService.get_orders(user)

    if isinstance(data, Exception):
        raise HTTPException(400, str(data))

    return data

@router.get('/orders/{order_id}')
async def order_info(order_id: int, user: TokenDataSchema = Depends(require_roles('admin'))) -> OrdersView:
    data = AdminService.get_order(order_id, user)

    if isinstance(data, Exception):
        raise HTTPException(400, str(data))

    return data

@router.put('/orders/{order_id}')
async def update_order(order_id: int, data: UpdateOrderSchema, user: TokenDataSchema = Depends(require_roles('admin'))) -> OrdersView:
    data = AdminService.update_order(order_id, data, user)

    if isinstance(data, Exception):
        raise HTTPException(400, str(data))

    return data

@router.post('/maintenances')
async def create_maintenance(data: CreateMaintenanceSchema, user: TokenDataSchema = Depends(require_roles('admin'))) -> MaintenancesView:
    data = AdminService.create_maintenance(data, user)

    if isinstance(data, Exception):
        raise HTTPException(400, str(data))

    return data

@router.get('/maintenances')
async def maintenances_list(user: TokenDataSchema = Depends(require_roles('admin'))) -> list[MaintenancesView]:
    data = AdminService.get_maintenances(user)

    if isinstance(data, Exception):
        raise HTTPException(400, str(data))

    return data

@router.get('/maintenances/{maintenance_id}')
async def maintenance_info(maintenance_id: int, user: TokenDataSchema = Depends(require_roles('admin'))) -> MaintenancesView:
    data = AdminService.get_maintenance(maintenance_id, user)

    if isinstance(data, Exception):
        raise HTTPException(400, str(data))

    return data

@router.delete('/maintenances/{maintenance_id}')
async def delete_maintenance(maintenance_id: int, user: TokenDataSchema = Depends(require_roles('admin'))) -> None:
    data = AdminService.delete_maintenance(maintenance_id, user)

    if isinstance(data, Exception):
        raise HTTPException(400, str(data))

    return data

@router.put('/maintenances/{maintenance_id}')
async def update_maintenance(maintenance_id: int, data: UpdateMaintenanceSchema, user: TokenDataSchema = Depends(require_roles('admin'))) -> MaintenancesView:
    data = AdminService.update_maintenance(maintenance_id, data, user)

    if isinstance(data, Exception):
        raise HTTPException(400, str(data))

    return data

@router.post('/transactions')
async def create_transaction(data: CreateTransactionSchema, user: TokenDataSchema = Depends(require_roles('admin'))) -> TransactionsView:
    data = AdminService.create_transaction(data, user)

    if isinstance(data, Exception):
        raise HTTPException(400, str(data))

    return data

@router.get('/transactions')
async def transactions_list(user: TokenDataSchema = Depends(require_roles('admin'))) -> list[TransactionsView]:
    data = AdminService.get_transactions(user)

    if isinstance(data, Exception):
        raise HTTPException(400, str(data))

    return data

@router.get('/transactions/{transaction_id}')
async def transaction_info(transaction_id: int, user: TokenDataSchema = Depends(require_roles('admin'))) -> TransactionsView:
    data = AdminService.get_transaction(transaction_id, user)

    if isinstance(data, Exception):
        raise HTTPException(400, str(data))

    return data
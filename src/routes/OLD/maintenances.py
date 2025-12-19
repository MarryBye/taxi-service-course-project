from fastapi import APIRouter, Depends, Request
from fastapi.responses import JSONResponse
from src.schemas.maintenances import MaintenanceSchema, CreateMaintenanceSchema, UpdateMaintenanceSchema
from src.schemas.token import TokenDataSchema
from src.controllers.maintenances import MaintenancesController
from src.dependencies.has_role import require_roles

router = APIRouter(prefix='/admin')

@router.get('/maintenances')
async def list(
        req: Request,
        current_user: TokenDataSchema = Depends(require_roles('admin'))
) -> list[MaintenanceSchema]:
    return MaintenancesController.list(req, current_user=current_user)

@router.get('/maintenances/{maintenance_id}')
async def get(
        req: Request,
        maintenance_id: int,
        current_user: TokenDataSchema = Depends(require_roles('admin'))
) -> MaintenanceSchema:
    return MaintenancesController.detail(req, maintenance_id=maintenance_id, current_user=current_user)

@router.post('/maintenances')
async def create(
        req: Request,
        schema: CreateMaintenanceSchema,
        current_user: TokenDataSchema = Depends(require_roles('admin'))
) -> JSONResponse:
    return MaintenancesController.create(req, schema=schema, current_user=current_user)

@router.put('/maintenances/{maintenance_id}')
async def update(
        req: Request,
        maintenance_id: int,
        schema: UpdateMaintenanceSchema,
        current_user: TokenDataSchema = Depends(require_roles('admin'))
) -> JSONResponse:
    return MaintenancesController.update(req, maintenance_id=maintenance_id, schema=schema, current_user=current_user)

@router.delete('/maintenances/{maintenance_id}')
async def delete(
        req: Request,
        maintenance_id: int,
        current_user: TokenDataSchema = Depends(require_roles('admin'))
) -> JSONResponse:
    return MaintenancesController.delete(req, maintenance_id=maintenance_id, current_user=current_user)


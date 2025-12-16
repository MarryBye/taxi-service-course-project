from fastapi import HTTPException, status, Request
from fastapi.responses import JSONResponse
from src.services.admin.maintenance_service import MaintenanceService
from src.schemas.maintenances import (
    MaintenanceSchema,
    CreateMaintenanceSchema,
    UpdateMaintenanceSchema
)
from src.schemas.token import TokenDataSchema


class MaintenancesController:

    @staticmethod
    def list(req: Request, current_user: TokenDataSchema) -> list[MaintenanceSchema]:
        result = MaintenanceService.list(user=current_user)

        if isinstance(result, Exception):
            raise HTTPException(400, str(result))

        if not result:
            raise HTTPException(404, "Maintenances not found")

        return result

    @staticmethod
    def detail(req: Request, maintenance_id: int, current_user: TokenDataSchema) -> MaintenanceSchema:
        result = MaintenanceService.get(maintenance_id, user=current_user)

        if isinstance(result, Exception):
            raise HTTPException(400, str(result))

        if not result:
            raise HTTPException(404, "Maintenance not found")

        return result

    @staticmethod
    def create(req: Request, schema: CreateMaintenanceSchema, current_user: TokenDataSchema) -> JSONResponse:
        result = MaintenanceService.create(schema, user=current_user)

        if isinstance(result, Exception):
            raise HTTPException(400, str(result))

        return JSONResponse({"detail": "Maintenance created successfully"}, status_code=200)

    @staticmethod
    def update(
        req: Request,
        maintenance_id: int,
        schema: UpdateMaintenanceSchema,
        current_user: TokenDataSchema
    ) -> JSONResponse:
        result = MaintenanceService.update(maintenance_id, schema, user=current_user)

        if isinstance(result, Exception):
            raise HTTPException(400, str(result))

        return JSONResponse({"detail": "Maintenance updated successfully"}, status_code=200)

    @staticmethod
    def delete(req: Request, maintenance_id: int, current_user: TokenDataSchema) -> JSONResponse:
        result = MaintenanceService.delete(maintenance_id, user=current_user)

        if isinstance(result, Exception):
            raise HTTPException(400, str(result))

        return JSONResponse({"detail": "Maintenance deleted successfully"}, status_code=200)

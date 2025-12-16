from fastapi import HTTPException, status, Request
from fastapi.responses import JSONResponse
from src.services.admin.cars_service import CarsService
from src.schemas.cars import CreateCarSchema, UpdateCarSchema, CarSchema
from src.schemas.token import TokenDataSchema


class CarsController:

    @staticmethod
    def list(req: Request, current_user: TokenDataSchema) -> list[CarSchema]:
        result = CarsService.list(user=current_user)

        if isinstance(result, Exception):
            raise HTTPException(400, str(result))

        if not result:
            raise HTTPException(404, "Cars not found")

        return result

    @staticmethod
    def detail(req: Request, car_id: int, current_user: TokenDataSchema) -> CarSchema:
        result = CarsService.get(car_id, user=current_user)

        if isinstance(result, Exception):
            raise HTTPException(400, str(result))

        if not result:
            raise HTTPException(404, "Car not found")

        return result

    @staticmethod
    def create(req: Request, schema: CreateCarSchema, current_user: TokenDataSchema) -> JSONResponse:
        result = CarsService.create(schema, user=current_user)

        if isinstance(result, Exception):
            raise HTTPException(400, str(result))

        return JSONResponse({"detail": "Car created successfully"}, status_code=200)

    @staticmethod
    def update(req: Request, car_id: int, schema: UpdateCarSchema, current_user: TokenDataSchema) -> JSONResponse:
        result = CarsService.update(car_id, schema, user=current_user)

        if isinstance(result, Exception):
            raise HTTPException(400, str(result))

        return JSONResponse({"detail": "Car updated successfully"}, status_code=200)

    @staticmethod
    def delete(req: Request, car_id: int, current_user: TokenDataSchema) -> JSONResponse:
        result = CarsService.delete(car_id, user=current_user)

        if isinstance(result, Exception):
            raise HTTPException(400, str(result))

        return JSONResponse({"detail": "Car deleted successfully"}, status_code=200)

from fastapi import HTTPException, status
from fastapi.responses import JSONResponse
from src.services.cars_service import CarsService
from src.schemas.cars import CarSchema, CarCreateSchema, CarUpdateSchema
from src.schemas.token import TokenDataSchema

class CarsController:
    @staticmethod
    def list_view(current_user: TokenDataSchema) -> list[CarSchema]:
        cars = CarsService.list()
        return cars
    
    @staticmethod
    def detail_view(car_id: int, current_user: TokenDataSchema) -> CarSchema:
        car = CarsService.get(car_id)
        if not car:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Car not found")
        return car

    @staticmethod
    def create_view(schema: CarCreateSchema, current_user: TokenDataSchema) -> CarSchema:
        car = CarsService.create(
            mark=schema.mark,
            model=schema.model,
            car_number=schema.car_number,
            car_class=schema.car_class,
            car_status=schema.car_status,
            driver_id=schema.driver_id
        )
        return car

    @staticmethod
    def update_view(car_id: int, schema: CarUpdateSchema, current_user: TokenDataSchema) -> CarSchema:
        car = CarsService.update(
            id=car_id,
            mark=schema.mark,
            model=schema.model,
            car_number=schema.car_number,
            car_class=schema.car_class,
            car_status=schema.car_status,
            driver_id=schema.driver_id
        )
        return car

    @staticmethod
    def delete_view(car_id: int, current_user: TokenDataSchema) -> None:
        CarsService.delete(car_id)
        return JSONResponse(status_code=status.HTTP_200_OK, content={"detail": "Car deleted successfully"})
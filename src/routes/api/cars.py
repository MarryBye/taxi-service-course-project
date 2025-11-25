from fastapi import APIRouter
from src.controllers.api.cars.index import ( list_view, update_view, delete_view, create_view, detail_view )

router = APIRouter()

router.add_api_route("/cars", list_view, methods=["GET"])
router.add_api_route("/cars", create_view, methods=["POST"])
router.add_api_route("/cars/{car_id}", detail_view, methods=["GET"])
router.add_api_route("/cars/{car_id}", update_view, methods=["PUT"])
router.add_api_route("/cars/{car_id}", delete_view, methods=["DELETE"])
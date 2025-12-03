from fastapi import APIRouter
from src.controllers.users import UsersController

router = APIRouter()

router.add_api_route("/users", UsersController.list_view, methods=["GET"])
router.add_api_route("/users", UsersController.create_view, methods=["POST"])
router.add_api_route("/users/{user_id}", UsersController.detail_view, methods=["GET"])
router.add_api_route("/users/{user_id}", UsersController.update_view, methods=["PUT"])
router.add_api_route("/users/{user_id}", UsersController.delete_view, methods=["DELETE"])
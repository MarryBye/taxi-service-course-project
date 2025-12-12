from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from src.schemas.profile import ProfileSchema, UpdateProfileSchema
from src.schemas.token import TokenDataSchema
from src.controllers.profile import ProfileController
from src.utils.auth import Auth

router = APIRouter()

@router.get('/profile')
async def get_profile(
        current_user: TokenDataSchema = Depends(Auth.verify_token)
) -> ProfileSchema:
    return ProfileController.detail_view(current_user=current_user)

@router.put('/profile')
async def update_profile(
        schema: UpdateProfileSchema,
        current_user: TokenDataSchema = Depends(Auth.verify_token)
) -> ProfileSchema:
    return ProfileController.update_view(schema=schema, current_user=current_user)

@router.delete('/profile')
async def delete_profile(
        current_user: TokenDataSchema = Depends(Auth.verify_token)
) -> JSONResponse:
    return ProfileController.delete_view(current_user=current_user)
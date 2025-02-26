from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from models.user_model import User
from services.auth_service import AuthService

router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("/signup/")
async def signup(user: User):
    return AuthService.signup(user)


@router.post("/signin/")
async def signin(form_data: OAuth2PasswordRequestForm = Depends()):
    return AuthService.signin(form_data)

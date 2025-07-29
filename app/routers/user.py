from fastapi import APIRouter, status, Depends, HTTPException
from app.models.user import UserCreate, UserResponse
from app.services.user_service import create_user

router = APIRouter()

@router.post("/register", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
async def register_user(user: UserCreate):
    # User creation logic will be implemented here
    pass

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from internal.shared.db import get_db
from internal.auth.dependencies import get_current_user
from .schemas import UserResponse

router = APIRouter(prefix="/users", tags=["users"])


@router.get("/me", response_model=UserResponse)
def me(current_user = Depends(get_current_user)):
    return current_user


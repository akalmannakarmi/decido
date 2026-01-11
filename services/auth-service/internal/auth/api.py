from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from internal.shared.db import get_db
from internal.auth.dependencies import get_current_service
from .schemas import RegisterRequest, LoginRequest, TokenResponse
from .service import AuthService

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/register", status_code=201)
def register(req: RegisterRequest, db: Session = Depends(get_db)):
    service = AuthService(db)
    try:
        service.register_user(req.email, req.password)
        return {"message": "User registered successfully"}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/login", response_model=TokenResponse)
def login(req: LoginRequest, db: Session = Depends(get_db)):
    service = AuthService(db)
    token = service.authenticate(req.email, req.password)
    return {
        "access_token": token,
        "token_type": "bearer",
    }


@router.post("/internal/verify-token")
def verify_token(
    token: str,
    service_name: str = Depends(get_current_service),
):
    payload = decode_access_token(token)
    return {
        "valid": True,
        "issued_to": payload.get("sub"),
        "verified_by": service_name,
    }

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from internal.shared.db import get_db
from internal.shared.security import decode_access_token
from internal.users.repo import UserRepo

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")


def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db),
):
    try:
        payload = decode_access_token(token)
        user_id: str | None = payload.get("sub")
        if user_id is None:
            raise ValueError("Invalid token payload")
    except ValueError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
        )

    repo = UserRepo(db)
    user = repo.get_by_id(int(user_id))

    if not user or not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User not found or inactive",
        )

    return user


def get_current_service(token: str = Depends(oauth2_scheme)):
    try:
        payload = decode_access_token(token)

        if payload.get("typ") != "service":
            raise ValueError("Not a service token")

        service_name = payload.get("sub")
        if service_name not in settings.allowed_services:
            raise ValueError("Unknown service")

        if payload.get("scope") != "internal":
            raise ValueError("Invalid service scope")

        return service_name

    except ValueError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid service credentials",
        )


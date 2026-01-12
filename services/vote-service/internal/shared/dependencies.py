from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

from .security import decode_access_token

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")


def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = decode_access_token(token)
        user_id: str | None = payload.get("sub")

        if user_id is None:
            raise ValueError("Invalid token payload")
        
        return int(user_id)
    except ValueError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
        )

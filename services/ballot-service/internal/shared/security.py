import jwt
from jwt import PyJWTError

from .config import settings


def decode_access_token(token: str) -> dict:
    try:
        return jwt.decode(
            token,
            settings.jwt_secret,
            algorithms=[settings.jwt_algorithm],
        )
    except PyJWTError:
        raise ValueError("Invalid or expired token")

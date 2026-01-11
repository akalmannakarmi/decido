from sqlalchemy.orm import Session

from internal.users.repo import UserRepo
from internal.users import domain as user_domain
from internal.shared import security


class AuthService:
    def __init__(self, db: Session):
        self.users = UserRepo(db)

    def register_user(self, email: str, password: str):
        user_domain.validate_email(email)
        user_domain.validate_password(password)

        if self.users.get_by_email(email):
            raise ValueError("Email already registered")

        password_hash = security.hash_password(password)
        user = self.users.create(email, password_hash)
        return user

    def authenticate(self, email: str, password: str) -> str:
        user = self.users.get_by_email(email)
        if not user:
            raise ValueError("Invalid credentials")

        if not security.verify_password(password, user.password_hash):
            raise ValueError("Invalid credentials")

        return security.create_access_token(subject=str(user.id))

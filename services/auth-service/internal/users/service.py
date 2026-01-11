from sqlalchemy.orm import Session
from .repo import UserRepo
from .domain import can_authenticate


class UserService:
    def __init__(self, db: Session):
        self.repo = UserRepo(db)

    def get_user(self, user_id: int):
        user = self.repo.get_by_id(user_id)
        if not user:
            raise ValueError("User not found")

        can_authenticate(user.is_active)
        return user

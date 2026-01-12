import re


def validate_email(email: str) -> None:
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        raise ValueError("Invalid email address")


def validate_password(password: str) -> None:
    if len(password) < 8:
        raise ValueError("Password must be at least 8 characters")

def can_authenticate(is_active: bool) -> None:
    if not is_active:
        raise ValueError("User is inactive")

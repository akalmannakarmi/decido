
def can_authenticate(is_active: bool) -> None:
    if not is_active:
        raise ValueError("User is inactive")


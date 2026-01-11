def can_modify_ballot(owner_id: int, user_id: int) -> None:
    if owner_id != user_id:
        raise ValueError("Not ballot owner")


def can_vote(is_active: bool) -> None:
    if not is_active:
        raise ValueError("Ballot is not active")

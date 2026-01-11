from sqlalchemy.orm import Session

from .repo import BallotRepo
from .domain import can_modify_ballot


class BallotService:
    def __init__(self, db: Session):
        self.repo = BallotRepo(db)

    def create_ballot(self, title: str, owner_id: int):
        return self.repo.create(title, owner_id)

    def list_ballots(self):
        return self.repo.list()

    def activate_ballot(self, ballot_id: int, user_id: int):
        ballot = self.repo.get(ballot_id)
        if not ballot:
            raise ValueError("Ballot not found")

        can_modify_ballot(ballot.owner_id, user_id)
        self.repo.activate(ballot)
        return ballot

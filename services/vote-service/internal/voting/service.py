import requests
from sqlalchemy.orm import Session

from internal.shared.config import settings
from .repo import VoteRepo
from .domain import ensure_ballot_active, ensure_not_voted


class VoteService:
    def __init__(self, db: Session):
        self.repo = VoteRepo(db)

    def cast_vote(self, ballot_id: int, user_id: int, choice: int):
        # resp = requests.gt(
        #     f"{settings.ballot_service_url}/ballots/{ballot_id}"
        # )
        #
        # if resp.status_code != 200:
        #     raise ValueError("Ballot not found")
        #
        # ballot = resp.json()
        # ensure_ballot_active(ballot["is_active"])

        ensure_not_voted(self.repo.has_voted(ballot_id, user_id))

        return self.repo.create_vote(ballot_id, user_id, choice)

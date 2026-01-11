from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import Session

from internal.shared.db import Base


class Ballot(Base):
    __tablename__ = "ballots"

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    owner_id = Column(Integer, nullable=False)
    is_active = Column(Boolean, default=False)


class BallotRepo:
    def __init__(self, db: Session):
        self.db = db

    def create(self, title: str, owner_id: int) -> Ballot:
        ballot = Ballot(title=title, owner_id=owner_id)
        self.db.add(ballot)
        self.db.commit()
        self.db.refresh(ballot)
        return ballot

    def get(self, ballot_id: int) -> Ballot | None:
        return self.db.query(Ballot).filter(Ballot.id == ballot_id).first()

    def list(self):
        return self.db.query(Ballot).all()

    def activate(self, ballot: Ballot):
        ballot.is_active = True
        self.db.commit()

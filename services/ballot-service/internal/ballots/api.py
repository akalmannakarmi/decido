from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from internal.shared.db import get_db
from internal.shared.dependencies import get_current_user
from .service import BallotService
from .schemas import BallotCreateRequest, BallotResponse

router = APIRouter(prefix="/ballots", tags=["ballots"])


@router.post("/", response_model=BallotResponse)
def create_ballot(
    req: BallotCreateRequest,
    user=Depends(get_current_user),
    db: Session = Depends(get_db),
):
    service = BallotService(db)
    return service.create_ballot(req.title, user["user_id"])


@router.get("/", response_model=list[BallotResponse])
def list_ballots(db: Session = Depends(get_db)):
    service = BallotService(db)
    return service.list_ballots()


@router.post("/{ballot_id}/activate", response_model=BallotResponse)
def activate_ballot(
    ballot_id: int,
    user=Depends(get_current_user),
    db: Session = Depends(get_db),
):
    service = BallotService(db)
    try:
        return service.activate_ballot(ballot_id, user["user_id"])
    except ValueError as e:
        raise HTTPException(status_code=403, detail=str(e))

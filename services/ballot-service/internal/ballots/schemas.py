from pydantic import BaseModel


class BallotCreateRequest(BaseModel):
    title: str


class BallotResponse(BaseModel):
    id: int
    title: str
    owner_id: int
    is_active: bool

from fastapi import FastAPI

from internal.ballots.api import router as ballot_router

app = FastAPI(title="Ballot Service")

app.include_router(ballot_router)


@app.get("/health")
def health():
    return {"status": "ok"}

from fastapi import FastAPI
from internal.auth.api import router as auth_router
from internal.users.api import router as users_router


app = FastAPI(title="Auth Service")

app.include_router(auth_router)
app.include_router(users_router)


@app.get("/health")
def health():
    return {"status": "ok"}


from fastapi import FastAPI
from app.api import api_router
from app.core.config import settings
from starlette.middleware.cors import CORSMiddleware


app = FastAPI(title=settings.PROJECT_NAME, debug=settings.DEBUG)

# Set all CORS enabled origins
if settings.all_cors_origins:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.all_cors_origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

app.include_router(api_router, prefix="/api/v1")

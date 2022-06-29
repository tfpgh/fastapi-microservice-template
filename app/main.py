from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from mangum import Mangum

from app import config
from app.middleware import EndpointExecutionTimeLoggingMiddleware
from app.routers import users

app = FastAPI(openapi_url="/openapi.json" if config.enable_docs else None)

app.add_middleware(
    CORSMiddleware,
    allow_origins=config.cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if config.profile_endpoints:
    app.add_middleware(EndpointExecutionTimeLoggingMiddleware)


app.include_router(users.router, prefix="/users")


@app.get("/")
async def root() -> str:
    return "Hello, Root!"


handler = Mangum(app)

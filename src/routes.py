from fastapi import FastAPI
from src.use_cases.create_auth.auth_controller import auth_router


def init_routes(app: FastAPI):
    app.include_router(auth_router)

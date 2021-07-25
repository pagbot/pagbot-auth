from fastapi import FastAPI
from src.use_cases.create_auth.auth_controller import auth_router
from src.use_cases.users import users_routes


def init_routes(app: FastAPI):
    app.include_router(auth_router)
    app.include_router(users_routes)

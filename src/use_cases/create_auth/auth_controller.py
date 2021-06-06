from fastapi import APIRouter

from src.settings import API_PREFIX
from src.repositories.implementations.auth import Auth

from .create_auth import CreateAuth


auth_router = APIRouter(prefix=API_PREFIX)


@auth_router.get("/gmail-auth")
async def do_gmail_auth():
    auth = Auth()
    create_auth = CreateAuth(auth)
    return await create_auth.create()


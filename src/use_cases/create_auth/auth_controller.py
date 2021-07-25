from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session

from src.infra.db.connection import get_db
from src.settings import API_PREFIX
from src.repositories.implementations.auth import Auth
from src.entities.schemas.user import UserSchema

from .create_auth import CreateAuth


auth_router = APIRouter(prefix=API_PREFIX)


@auth_router.post("/gmail-auth", response_model=UserSchema, status_code=201)
async def do_gmail_auth(db: Session = Depends(get_db)):
    auth = Auth(db)
    create_auth = CreateAuth(auth)
    return await create_auth.create()


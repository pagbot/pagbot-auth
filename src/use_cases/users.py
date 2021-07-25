from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session

from src.infra.db.connection import get_db
from src.settings import API_PREFIX
from src.repositories.implementations.users.retieve import RetrieveUser
from src.repositories.implementations.users.list import ListUsers
from src.entities.schemas.user import UserSchema


users_routes = APIRouter(prefix=API_PREFIX)


@users_routes.get("/users/{uuid}", response_model=UserSchema)
async def retrieve_user(uuid: str, db: Session = Depends(get_db)):
    user = RetrieveUser(db)
    return await user.get(uuid)


@users_routes.get("/users", response_model=UserSchema)
async def list_users(db: Session = Depends(get_db)):
    users = ListUsers(db)
    return await users.list()

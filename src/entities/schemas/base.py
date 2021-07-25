from pydantic import BaseModel


class BaseSchema(BaseModel):
    errors: list
    message: str

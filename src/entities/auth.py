import uuid

from sqlalchemy import String, Column
from sqlalchemy_utils import EmailType
from sqlalchemy.dialects.postgresql import UUID

from src.infra.db.setup import Base


class Auth(Base):
    __tablename__ = "auth"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_email = Column(EmailType)
    token = Column(String)
    refresh_token = Column(String)
    client_id = Column(String)
    client_secret = Column(String)
    expiry = Column(String)

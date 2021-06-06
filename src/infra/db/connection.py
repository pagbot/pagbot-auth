from src.infra.db.setup import Session


def connect_db():
    db = Session()
    try:
        return db
    finally:
        db.close()

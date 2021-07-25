from fastapi.responses import JSONResponse

from src.entities.auth import Auth as AuthTable


class RetrieveUser:
    def __init__(self, db):
        self.db = db

    async def get(self, uuid: str):
        user = self.db.query(
            AuthTable
        ).filter_by(id=uuid).first()
        if not user:
            return JSONResponse({
                'data': [],
                "errors": [],
                "message": "Not Found"
            }, status_code=404)
        return {
            'data': [{
                'id': str(user.id),
                'email': user.email,
                'token': user.token
            }],
            "errors": [],
            "message": "Success"
        }

from fastapi.responses import JSONResponse

from src.entities.auth import Auth as AuthTable


class ListUsers:

    def __init__(self, db_connection):
        self.db_connection = db_connection

    async def list(self):
        users = self.db_connection.query(AuthTable).all()
        if not users:
            return JSONResponse({
                'data': [],
                "errors": [],
                "message": "Not Found"
            }, status_code=404)

        return {
            'data': [
                {
                    'id': user.id,
                    'email': user.email,
                    'token': user.token
                }
                for user in users
            ],
            "errors": [],
            "message": "Success"
        }

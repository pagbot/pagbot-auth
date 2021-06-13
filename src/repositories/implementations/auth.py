import json

from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from fastapi.responses import JSONResponse

from src.repositories.interfaces.auth import IAuth
from src.infra.db.connection import connect_db
from src.entities.auth import Auth as AuthTable
from src.settings import GOOGLE_API


class Auth(IAuth):
    db = connect_db()

    @staticmethod
    def start_config():
        return {
              "web": {
                "client_id": GOOGLE_API['CLIENT_ID'],
                "project_id": "pagbot",
                "auth_uri": "https://accounts.google.com/o/oauth2/auth",
                "token_uri": "https://oauth2.googleapis.com/token",
                "auth_provider_x509_cert_url": (
                    "https://www.googleapis.com/oauth2/v1/certs"
                ),
                "client_secret": GOOGLE_API['CLIENT_SECRET']
              }
        }

    async def create_auth(self, data):
        auth = AuthTable(**data)
        self.db.add(auth)
        self.db.commit()

    async def has_user(self, user_email):
        return bool(self.db.query(
            AuthTable
        ).filter_by(user_email=user_email).first())

    @staticmethod
    async def watch_user(gmail):
        request = {
            'labelIds': ['INBOX', 'IMPORTANT'],
            'topicName': 'projects/pagbot/topics/gmail'
        }
        gmail.users().watch(userId='me', body=request).execute()

    async def create(self):
        config = self.start_config()
        flow = InstalledAppFlow.from_client_config(
            config, ['https://mail.google.com/']
        )
        creds = flow.run_local_server(port=2222)
        gmail = build('gmail', 'v1', credentials=creds)
        user_email = gmail.users().getProfile(userId='me').execute()

        json_creds = json.loads(creds.to_json())
        json_creds.pop('token_uri')
        json_creds.pop('scopes')
        json_creds['user_email'] = user_email["emailAddress"]

        user = await self.has_user(json_creds['user_email'])
        if not user:
            await self.watch_user(gmail)
            await self.create_auth(json_creds)
            return JSONResponse({
                'data': [{
                    'userEmail': json_creds['user_email'],
                    'authToken': json_creds['token']
                }],
                "errors": [],
                "status": 200,
                "message": "Success"
            })
        return JSONResponse(
            content={
                'data': [],
                "errors": [{'message': 'User already exists'}],
                "status": 400,
                "message": "Database Error"
            },
            status_code=400
        )

from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build


SCOPES = ['https://mail.google.com/']


def main():
    flow = InstalledAppFlow.from_client_secrets_file(
        'credentials.json', SCOPES
    )
    creds = flow.run_local_server(port=2222)
    print(creds.to_json())
    gmail = build('gmail', 'v1', credentials=creds)
    user_email = gmail.users().getProfile(userId='me').execute()
    print(f'User Email: {user_email["emailAddress"]}')


if __name__ == '__main__':
    main()


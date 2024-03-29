from decouple import config
from src import __version__


API_PREFIX = f'/api/{__version__}'

DATABASE_URL = config('DATABASE_URL')

APP = {
    'HOST': config('HOST', default='0.0.0.0'),
    'PORT': config('PORT', cast=int, default='8080')
}

GOOGLE_API = {
    'CLIENT_ID': config('GOOGLE_CLIENT_ID'),
    'CLIENT_SECRET': config('GOOGLE_CLIENT_SECRET')
}

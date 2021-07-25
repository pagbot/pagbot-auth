from uvicorn import run
from fastapi import FastAPI

from src.settings import APP
from src.routes import init_routes
from src.infra.db.setup import init_db


app = FastAPI()

init_db()
init_routes(app)


if __name__ == "__main__":
    run('app:app', host=APP['HOST'], port=APP['PORT'], reload=True)


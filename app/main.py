from fastapi import FastAPI

from app.db import create_db_and_tables
from app.api.api import api_router


app = FastAPI(title='Simple time management')
app.include_router(api_router, prefix='/api')


@app.on_event("startup")
def on_startup():
    create_db_and_tables()

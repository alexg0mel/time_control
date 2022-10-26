from fastapi import FastAPI

from app.db import create_db_and_tables

app = FastAPI()


@app.on_event("startup")
def on_startup():
    create_db_and_tables()


@app.get('/')
def get_main_view():
    return {'hello: dude!'}


from fastapi import FastAPI

app = FastAPI()


@app.on_event("startup")
def on_startup():
    ...


@app.get('/')
def get_main_view():
    return {'hello: dude!'}


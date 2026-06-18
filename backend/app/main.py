from fastapi import FastAPI
from . import models
from .db import engine
from .controllers import router as controllers_router

app = FastAPI(title='Cashback API')

app.include_router(controllers_router)


@app.on_event('startup')
def startup():
    # Cria tabelas
    models.Base.metadata.create_all(bind=engine)


@app.get('/')
def root():
    return {'status': 'ok', 'service': 'cashback-api'}

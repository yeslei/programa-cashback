from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os
from . import models
from .db import engine
from .controllers import router as controllers_router

app = FastAPI(title='Cashback API')

frontend_url = os.getenv('FRONTEND_URL')
allowed_origins = [
    'http://localhost:4200',
    'http://127.0.0.1:4200',
]
if frontend_url:
    allowed_origins.append(frontend_url)

app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

app.include_router(controllers_router)


@app.on_event('startup')
def startup():
    # Cria tabelas
    models.Base.metadata.create_all(bind=engine)


@app.get('/')
def root():
    return {'status': 'ok', 'service': 'cashback-api'}

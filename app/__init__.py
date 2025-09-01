# app/__init__.py

import logging
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.configuration.settings import Configuration
from app.api import register_routes

configuration = Configuration()

def create_app():
    app = FastAPI()

    logging.debug("SISTEMA >>> Inicializando...")

    origins = (
        [configuration.base_url]
        if configuration.environment == "production"
        else [configuration.base_url_dev]
    )
    logging.debug(f"CORS origins configuradas: {origins}")
    logging.debug(f"Ambiente atual: {configuration.environment}")

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
        expose_headers=["X-Filename"],
    )
    logging.debug("Middleware CORS adicionado")

    register_routes(app)
    logging.debug("Rotas registradas com sucesso")

    return app

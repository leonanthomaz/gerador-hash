# app/api/routes/sandbox_router.py

import logging
from fastapi import APIRouter, HTTPException
from jose import jwt, JWTError
from datetime import datetime, timedelta
import redis
import os

from app.configuration.settings import Configuration

configuration = Configuration()

# Config Redis
REDIS_URL = os.getenv("REDIS_URL")
if not REDIS_URL:
    raise RuntimeError("REDIS_URL não definido no .env")

r = redis.from_url(REDIS_URL, decode_responses=True)
logging.debug(f"Redis conectado em {REDIS_URL}")

# Config JWT
SECRET_KEY = os.getenv("AUTH_JWT_SECRET_KEY", "chave_segura")
ALGORITHM = "HS256"
EXPIRATION_HOURS = int(os.getenv("AUTH_JWT_EXPIRATION_HOURS", 24))
logging.debug(f"Config JWT -> Algoritmo: {ALGORITHM}, Expiração: {EXPIRATION_HOURS}h")

class SandboxRouter(APIRouter):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        logging.debug("SandboxRouter inicializado")

        self.add_api_route(
            "/generate-token/{project_id}", self.generate_token, methods=["POST"]
        )
        self.add_api_route(
            "/validate-token/{token}", self.validate_token, methods=["POST"]
        )

    async def generate_token(self, project_id: str):
        logging.debug(f"Gerando token para projeto: {project_id}")
        project_id_upper = project_id.upper()

        expire = datetime.utcnow() + timedelta(hours=EXPIRATION_HOURS)
        payload = {
            "project_id": project_id_upper,
            "exp": expire,
        }
        token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
        logging.debug(f"Payload JWT criado: {payload}")

        ttl_seconds = EXPIRATION_HOURS * 3600
        r.setex(f"sandbox:token:{token}", ttl_seconds, project_id_upper)
        logging.debug(f"Token salvo no Redis com TTL de {ttl_seconds}s")

        logging.debug(f"Token gerado para projeto {project_id}, expira em {EXPIRATION_HOURS}h")
        return {
            "token": token,
            "url": f"{configuration.base_url}/{project_id}/{token}",
        }

    async def validate_token(self, token: str):
        logging.debug(f"Validando token: {token}")
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
            project_id = payload.get("project_id")
            logging.debug(f"Payload decodificado: {payload}")
        except JWTError:
            logging.debug("Falha ao decodificar token")
            raise HTTPException(status_code=401, detail="Token inválido")

        saved_project = r.get(f"sandbox:token:{token}")
        if not saved_project or saved_project != project_id:
            logging.debug(f"Token expirado ou inválido no Redis: {saved_project}")
            raise HTTPException(status_code=401, detail="Token expirado ou inválido")

        logging.debug(f"Token válido para projeto {project_id}")
        return {"status": "Token Aceito."}


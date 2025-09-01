# app/configuration/settings.py

import logging
import os
from dotenv import load_dotenv

# Configuração de logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Carrega as variáveis de ambiente
load_dotenv(dotenv_path=".env", encoding="utf-8")

class Configuration:
    def __init__(self):
        
        # Url base
        self.base_url = os.getenv("APP_WEB_URL", "http://localhost:3000")
        self.base_url_dev = os.getenv("APP_WEB_URL_DEV", "http://localhost:3000")

        # Configurações do ambiente e banco de dados
        self.environment = os.getenv("APP_ENVIRONMENT_DEFAULT", "development").lower()

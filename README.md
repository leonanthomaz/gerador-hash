# 🛠 Sandbox Token Generator - FastAPI + Redis + JWT

Projeto simples de **geração e validação de tokens JWT** usando **FastAPI** e **Redis**, ideal para iniciantes que querem ver como integrar backend moderno com armazenamento em memória.  

---

## Estrutura do Projeto
```bash
projeto/
├── app/
│ ├── init.py # Cria app FastAPI e configura CORS
│ ├── api/
│ │ ├── routes/
│ │ │ ├── init.py # Registra rotas
│ │ │ └── sandbox_router.py # Router de geração/validação de token
│ └── configuration/
│ └── settings.py # Configurações de ambiente e logging
├── main.py # Inicializa servidor
└── README.md
```
---

## ⚙️ Tecnologias
- **Python 3.9+**  
- [FastAPI](https://fastapi.tiangolo.com/) → Framework web moderno  
- [Redis](https://redis.io/) → Armazenamento em memória  
- [JWT (PyJWT / jose)](https://python-jose.readthedocs.io/) → Tokens seguros  
- [Uvicorn](https://www.uvicorn.org/) → Servidor ASGI

---

## Como Rodar

### 1. Clone o repositório
```bash
git clone https://github.com/leonanthomaz/sandbox-token.git
cd sandbox-token
```

### 2. Crie e ative o ambiente virtual
```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```

### 3. Instale as dependências
```bash
pip install fastapi uvicorn python-jose redis python-dotenv
```

### 4. Configure o .env
Crie um arquivo .env na raiz com as variáveis:

env:
```bash
REDIS_URL=redis://localhost:6379/0
AUTH_JWT_SECRET_KEY=sua_chave_super_secreta
AUTH_JWT_EXPIRATION_HOURS=24
APP_WEB_URL=http://localhost:3000
APP_WEB_URL_DEV=http://localhost:3000
APP_ENVIRONMENT_DEFAULT=development
```

```bash
🔹 REDIS_URL → conexão com Redis
🔹 AUTH_JWT_SECRET_KEY → chave para assinar tokens
🔹 AUTH_JWT_EXPIRATION_HOURS → validade do token em horas
🔹 URLs e ambiente → para CORS e dev/prod
```

### 5. Rode a aplicação
```bash
python main.py
API disponível em:
👉 http://127.0.0.1:5000
```

---

📖 Endpoints
```bash
POST /generate-token/{project_id} → Gera token JWT para o projeto
```

---

### Response
```bash
{
  "token": "<token_gerado>",
  "url": "http://localhost:3000/PROJETO/<token_gerado>"
}
POST /validate-token/{token} → Valida token JWT
```

---

### Response
```bash
{
  "status": "Token Aceito."
}
```

### Use Swagger UI para testar interativamente.

---

💡 Dicas para iniciantes
- Configure o Redis antes de rodar a aplicação (docker run -p 6379:6379 redis)
- Observe os logs em DEBUG para entender o fluxo de geração e validação do token
- Tokens expiram automaticamente após AUTH_JWT_EXPIRATION_HOURS horas
- Esse projeto é modular: FastAPI + routers + configuração separada → padrão profissional

## Contato

Desenvolvedor: Leonan Thomaz
Email: leonan.thomaz@gmail.com

#### Redes Sociais

- LinkedIn: https://www.linkedin.com/in/leonanthomaz
- GitHub: https://github.com/leonanthomaz


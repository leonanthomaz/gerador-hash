# app/routes/__init__.py

from app.api.routes.sandbox import SandboxRouter

def register_routes(app):
    app.include_router(SandboxRouter())

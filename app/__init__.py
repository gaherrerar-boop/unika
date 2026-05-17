"""Fábrica de aplicación FastAPI para Unika."""
import os
from pathlib import Path

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from starlette.middleware.sessions import SessionMiddleware

from app.database.session import init_db
from app.routes import admin, contact, content, main as main_routes, products
from app.templates import templates

BASE_DIR = Path(__file__).resolve().parent


def create_app() -> FastAPI:
    app = FastAPI(
        title="Unika — Tejidos a mano",
        description="Marca artesanal chilena de carteras, chalecos y accesorios tejidos a mano.",
        version="1.0.0",
    )

    secret_key = os.getenv("SECRET_KEY", "unika-dev-secret")
    app.add_middleware(SessionMiddleware, secret_key=secret_key)

    static_dir = BASE_DIR / "static"
    app.mount("/static", StaticFiles(directory=static_dir), name="static")

    @app.on_event("startup")
    def _startup() -> None:
        init_db()

    @app.exception_handler(404)
    async def not_found(request: Request, exc):
        return templates.TemplateResponse(
            "errors/404.html",
            {"request": request, "title": "Página no encontrada"},
            status_code=404,
        )

    @app.exception_handler(500)
    async def server_error(request: Request, exc):
        return JSONResponse(
            status_code=500,
            content={"detail": "Algo no salió bien. Estamos tejiendo la solución."},
        )

    app.include_router(main_routes.router)
    app.include_router(products.router)
    app.include_router(contact.router)
    app.include_router(content.router)
    app.include_router(admin.router)

    return app

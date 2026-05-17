"""Punto de entrada de la aplicación Unika."""
import os

import uvicorn
from dotenv import load_dotenv

load_dotenv()

from app import create_app

app = create_app()


if __name__ == "__main__":
    host = os.getenv("APP_HOST", "127.0.0.1")
    port = int(os.getenv("APP_PORT", "8000"))
    reload = os.getenv("APP_ENV", "development") == "development"
    uvicorn.run("main:app", host=host, port=port, reload=reload)

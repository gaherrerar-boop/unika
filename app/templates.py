"""Configuración compartida de Jinja2."""
from pathlib import Path

from fastapi.templating import Jinja2Templates

from app.config import settings

TEMPLATES_DIR = Path(__file__).resolve().parent / "templates"

templates = Jinja2Templates(directory=str(TEMPLATES_DIR))

templates.env.globals["brand"] = {
    "name": settings.app_name,
    "tagline": "Tejido a mano, hecho con tiempo.",
    "email": settings.contact_email,
    "phone": settings.contact_phone,
    "instagram": settings.instagram_url,
    "facebook": settings.facebook_url,
    "tiktok": settings.tiktok_url,
}

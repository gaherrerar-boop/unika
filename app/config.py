"""Configuración global de la aplicación."""
import os
from dataclasses import dataclass


@dataclass(frozen=True)
class Settings:
    app_name: str = os.getenv("APP_NAME", "Unika")
    contact_email: str = os.getenv("CONTACT_EMAIL", "hola@unika.cl")
    contact_phone: str = os.getenv("CONTACT_PHONE", "+56 9 0000 0000")
    instagram_url: str = os.getenv("INSTAGRAM_URL", "https://instagram.com/unika")
    facebook_url: str = os.getenv("FACEBOOK_URL", "https://facebook.com/unika")
    tiktok_url: str = os.getenv("TIKTOK_URL", "https://tiktok.com/@unika")
    admin_user: str = os.getenv("ADMIN_USER", "admin")
    admin_password: str = os.getenv("ADMIN_PASSWORD", "unika2026")


settings = Settings()

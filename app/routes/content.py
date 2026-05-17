"""Rutas de contenido editorial / redes sociales."""
from fastapi import APIRouter, Request

from app.content.social import SOCIAL_CONTENT
from app.templates import templates

router = APIRouter()


@router.get("/redes")
def social_content(request: Request):
    return templates.TemplateResponse(
        "pages/social.html",
        {
            "request": request,
            "title": "Contenido para redes — Unika",
            "page": "social",
            "social": SOCIAL_CONTENT,
        },
    )

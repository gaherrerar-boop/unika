"""Rutas principales: home, hecho a mano, proceso, galería."""
from fastapi import APIRouter, Depends, Request
from sqlalchemy.orm import Session

from app.content.brand import BRAND_COPY, HANDMADE_BLOCKS, PROCESS_STEPS, GALLERY_ITEMS
from app.database.session import get_db
from app.services.products import list_products
from app.templates import templates

router = APIRouter()


@router.get("/")
def home(request: Request, db: Session = Depends(get_db)):
    featured = list_products(db, featured=True, limit=4)
    latest = list_products(db, limit=8)
    return templates.TemplateResponse(
        "pages/home.html",
        {
            "request": request,
            "title": "Unika — Tejidos a mano",
            "page": "home",
            "featured": featured,
            "latest": latest,
            "brand_copy": BRAND_COPY,
            "process_steps": PROCESS_STEPS[:3],
        },
    )


@router.get("/hecho-a-mano")
def handmade(request: Request):
    return templates.TemplateResponse(
        "pages/handmade.html",
        {
            "request": request,
            "title": "Hecho a mano — Unika",
            "page": "handmade",
            "blocks": HANDMADE_BLOCKS,
            "brand_copy": BRAND_COPY,
        },
    )


@router.get("/proceso")
def process(request: Request):
    return templates.TemplateResponse(
        "pages/process.html",
        {
            "request": request,
            "title": "Proceso creativo — Unika",
            "page": "process",
            "steps": PROCESS_STEPS,
            "brand_copy": BRAND_COPY,
        },
    )


@router.get("/galeria")
def gallery(request: Request):
    return templates.TemplateResponse(
        "pages/gallery.html",
        {
            "request": request,
            "title": "Galería — Unika",
            "page": "gallery",
            "items": GALLERY_ITEMS,
        },
    )

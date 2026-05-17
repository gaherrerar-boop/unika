"""Rutas de catálogo y ficha de producto."""
from fastapi import APIRouter, Depends, HTTPException, Request
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.services.products import (
    get_product_by_slug,
    list_categories,
    list_products,
    related_products,
)
from app.templates import templates

router = APIRouter()

CATEGORY_LABELS = {
    "todas": "Todas",
    "carteras": "Carteras",
    "chalecos": "Chalecos",
    "accesorios": "Accesorios",
}


@router.get("/catalogo")
def catalog(request: Request, categoria: str = "todas", db: Session = Depends(get_db)):
    products = list_products(db, category=categoria)
    categories = list_categories(db)
    return templates.TemplateResponse(
        "pages/catalog.html",
        {
            "request": request,
            "title": "Catálogo — Unika",
            "page": "catalog",
            "products": products,
            "categories": ["todas", *categories],
            "category_labels": CATEGORY_LABELS,
            "active_category": categoria,
        },
    )


@router.get("/producto/{slug}")
def product_detail(slug: str, request: Request, db: Session = Depends(get_db)):
    product = get_product_by_slug(db, slug)
    if not product:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    related = related_products(db, product, limit=3)
    return templates.TemplateResponse(
        "pages/product.html",
        {
            "request": request,
            "title": f"{product.name} — Unika",
            "page": "product",
            "product": product,
            "related": related,
        },
    )

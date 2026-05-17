"""Servicios de dominio para productos."""
from __future__ import annotations

import re
from typing import Iterable

from sqlalchemy.orm import Session

from app.models.product import Product


def slugify(value: str) -> str:
    value = value.lower().strip()
    value = re.sub(r"[áàä]", "a", value)
    value = re.sub(r"[éèë]", "e", value)
    value = re.sub(r"[íìï]", "i", value)
    value = re.sub(r"[óòö]", "o", value)
    value = re.sub(r"[úùü]", "u", value)
    value = re.sub(r"ñ", "n", value)
    value = re.sub(r"[^a-z0-9\s-]", "", value)
    value = re.sub(r"\s+", "-", value)
    value = re.sub(r"-+", "-", value)
    return value.strip("-") or "producto"


def list_products(
    db: Session,
    category: str | None = None,
    featured: bool | None = None,
    limit: int | None = None,
) -> list[Product]:
    q = db.query(Product)
    if category and category != "todas":
        q = q.filter(Product.category == category)
    if featured is not None:
        q = q.filter(Product.featured == featured)
    q = q.order_by(Product.featured.desc(), Product.created_at.desc())
    if limit:
        q = q.limit(limit)
    return q.all()


def get_product_by_slug(db: Session, slug: str) -> Product | None:
    return db.query(Product).filter(Product.slug == slug).first()


def get_product(db: Session, product_id: int) -> Product | None:
    return db.query(Product).filter(Product.id == product_id).first()


def list_categories(db: Session) -> list[str]:
    rows = db.query(Product.category).distinct().all()
    return sorted({row[0] for row in rows})


def create_product(db: Session, data: dict) -> Product:
    base_slug = slugify(data.get("slug") or data["name"])
    slug = base_slug
    suffix = 2
    while db.query(Product).filter(Product.slug == slug).first() is not None:
        slug = f"{base_slug}-{suffix}"
        suffix += 1
    data["slug"] = slug
    product = Product(**data)
    db.add(product)
    db.commit()
    db.refresh(product)
    return product


def update_product(db: Session, product: Product, data: dict) -> Product:
    for key, value in data.items():
        if hasattr(product, key) and value is not None:
            setattr(product, key, value)
    db.commit()
    db.refresh(product)
    return product


def delete_product(db: Session, product: Product) -> None:
    db.delete(product)
    db.commit()


def related_products(db: Session, product: Product, limit: int = 3) -> list[Product]:
    return (
        db.query(Product)
        .filter(Product.category == product.category, Product.id != product.id)
        .limit(limit)
        .all()
    )


def categories_with_counts(products: Iterable[Product]) -> dict[str, int]:
    counts: dict[str, int] = {}
    for product in products:
        counts[product.category] = counts.get(product.category, 0) + 1
    return counts

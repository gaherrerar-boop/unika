"""Modelo de producto tejido a mano."""
from datetime import datetime

from sqlalchemy import Boolean, Column, DateTime, Float, Integer, String, Text

from app.database.session import Base


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    slug = Column(String(160), unique=True, index=True, nullable=False)
    name = Column(String(160), nullable=False)
    category = Column(String(60), index=True, nullable=False)
    short_description = Column(String(280), nullable=False)
    description = Column(Text, nullable=False)
    materials = Column(String(280), nullable=False)
    color = Column(String(80), nullable=False)
    dimensions = Column(String(140), nullable=False, default="")
    price = Column(Float, nullable=False, default=0.0)
    stock = Column(Integer, nullable=False, default=1)
    image = Column(String(255), nullable=False, default="/static/img/placeholder.svg")
    gallery = Column(Text, nullable=False, default="")  # urls separadas por coma
    featured = Column(Boolean, default=False, nullable=False)
    handmade_hours = Column(Integer, nullable=False, default=0)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)

    @property
    def gallery_list(self) -> list[str]:
        if not self.gallery:
            return []
        return [item.strip() for item in self.gallery.split(",") if item.strip()]

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "slug": self.slug,
            "name": self.name,
            "category": self.category,
            "short_description": self.short_description,
            "description": self.description,
            "materials": self.materials,
            "color": self.color,
            "dimensions": self.dimensions,
            "price": self.price,
            "stock": self.stock,
            "image": self.image,
            "gallery": self.gallery_list,
            "featured": self.featured,
            "handmade_hours": self.handmade_hours,
        }

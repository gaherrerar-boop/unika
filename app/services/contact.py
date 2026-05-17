"""Servicios para la gestión de mensajes y pedidos personalizados."""
from __future__ import annotations

from sqlalchemy.orm import Session

from app.models.message import Message


def create_message(db: Session, data: dict) -> Message:
    msg = Message(**data)
    db.add(msg)
    db.commit()
    db.refresh(msg)
    return msg


def list_messages(db: Session, limit: int = 50) -> list[Message]:
    return (
        db.query(Message)
        .order_by(Message.created_at.desc())
        .limit(limit)
        .all()
    )

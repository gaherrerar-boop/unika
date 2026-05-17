"""Modelo de mensajes de contacto / pedidos personalizados."""
from datetime import datetime

from sqlalchemy import Column, DateTime, Integer, String, Text

from app.database.session import Base


class Message(Base):
    __tablename__ = "messages"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(120), nullable=False)
    email = Column(String(160), nullable=False)
    phone = Column(String(40), nullable=False, default="")
    subject = Column(String(160), nullable=False, default="Consulta general")
    message = Column(Text, nullable=False)
    kind = Column(String(40), nullable=False, default="consulta")  # consulta | pedido
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)

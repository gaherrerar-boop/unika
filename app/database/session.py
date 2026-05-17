"""Motor y sesión de SQLAlchemy + inicialización con datos semilla."""
import os
from pathlib import Path

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

if os.getenv("VERCEL"):
    DB_DIR = Path("/tmp")
else:
    DB_DIR = Path(__file__).resolve().parent
DB_DIR.mkdir(parents=True, exist_ok=True)

DEFAULT_DB_URL = f"sqlite:///{(DB_DIR / 'unika.db').as_posix()}"
DATABASE_URL = os.getenv("DATABASE_URL", DEFAULT_DB_URL)

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False} if DATABASE_URL.startswith("sqlite") else {},
    future=True,
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine, future=True)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def init_db() -> None:
    """Crea las tablas y carga datos semilla si la base está vacía."""
    from app.models.product import Product  # noqa: F401
    from app.models.message import Message  # noqa: F401
    from app.database.seed import seed_products

    Base.metadata.create_all(bind=engine)
    seed_products()

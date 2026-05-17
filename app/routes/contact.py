"""Rutas de contacto y pedidos personalizados."""
from fastapi import APIRouter, Depends, Form, Request
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.services.contact import create_message
from app.templates import templates

router = APIRouter()


@router.get("/contacto")
def contact_page(request: Request, ok: int = 0):
    return templates.TemplateResponse(
        "pages/contact.html",
        {
            "request": request,
            "title": "Contacto — Unika",
            "page": "contact",
            "success": bool(ok),
        },
    )


@router.post("/contacto")
def contact_submit(
    request: Request,
    name: str = Form(...),
    email: str = Form(...),
    phone: str = Form(""),
    subject: str = Form("Consulta general"),
    message: str = Form(...),
    kind: str = Form("consulta"),
    db: Session = Depends(get_db),
):
    create_message(
        db,
        {
            "name": name.strip(),
            "email": email.strip(),
            "phone": phone.strip(),
            "subject": subject.strip() or "Consulta general",
            "message": message.strip(),
            "kind": kind if kind in {"consulta", "pedido"} else "consulta",
        },
    )
    return RedirectResponse(url="/contacto?ok=1", status_code=303)

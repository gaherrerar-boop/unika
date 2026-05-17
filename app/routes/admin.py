"""Dashboard simple de administración (CRUD básico de productos)."""
from fastapi import APIRouter, Depends, Form, HTTPException, Request
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session

from app.config import settings
from app.database.session import get_db
from app.services.contact import list_messages
from app.services.products import (
    create_product,
    delete_product,
    get_product,
    list_products,
    update_product,
)
from app.templates import templates

router = APIRouter(prefix="/admin", tags=["admin"])


def _is_authenticated(request: Request) -> bool:
    return bool(request.session.get("admin"))


def _require_admin(request: Request) -> RedirectResponse | None:
    if not _is_authenticated(request):
        return RedirectResponse(url="/admin/login", status_code=303)
    return None


@router.get("/login")
def login_page(request: Request, error: int = 0):
    if _is_authenticated(request):
        return RedirectResponse(url="/admin", status_code=303)
    return templates.TemplateResponse(
        "admin/login.html",
        {
            "request": request,
            "title": "Acceso administración — Unika",
            "page": "admin",
            "error": bool(error),
        },
    )


@router.post("/login")
def login_submit(
    request: Request,
    user: str = Form(...),
    password: str = Form(...),
):
    if user == settings.admin_user and password == settings.admin_password:
        request.session["admin"] = True
        return RedirectResponse(url="/admin", status_code=303)
    return RedirectResponse(url="/admin/login?error=1", status_code=303)


@router.get("/logout")
def logout(request: Request):
    request.session.pop("admin", None)
    return RedirectResponse(url="/admin/login", status_code=303)


@router.get("")
@router.get("/")
def dashboard(request: Request, db: Session = Depends(get_db)):
    redirect = _require_admin(request)
    if redirect:
        return redirect
    products = list_products(db)
    messages = list_messages(db, limit=20)
    return templates.TemplateResponse(
        "admin/dashboard.html",
        {
            "request": request,
            "title": "Administración — Unika",
            "page": "admin",
            "products": products,
            "messages": messages,
        },
    )


@router.get("/productos/nuevo")
def new_product_form(request: Request):
    redirect = _require_admin(request)
    if redirect:
        return redirect
    return templates.TemplateResponse(
        "admin/product_form.html",
        {
            "request": request,
            "title": "Nuevo producto — Unika",
            "page": "admin",
            "product": None,
            "form_action": "/admin/productos",
        },
    )


@router.post("/productos")
def create_product_submit(
    request: Request,
    name: str = Form(...),
    category: str = Form(...),
    short_description: str = Form(...),
    description: str = Form(...),
    materials: str = Form(...),
    color: str = Form(...),
    dimensions: str = Form(""),
    price: float = Form(...),
    stock: int = Form(1),
    image: str = Form("/static/img/placeholder.svg"),
    gallery: str = Form(""),
    featured: str = Form(""),
    handmade_hours: int = Form(0),
    db: Session = Depends(get_db),
):
    redirect = _require_admin(request)
    if redirect:
        return redirect
    create_product(
        db,
        {
            "name": name.strip(),
            "category": category.strip().lower(),
            "short_description": short_description.strip(),
            "description": description.strip(),
            "materials": materials.strip(),
            "color": color.strip(),
            "dimensions": dimensions.strip(),
            "price": price,
            "stock": stock,
            "image": image.strip() or "/static/img/placeholder.svg",
            "gallery": gallery.strip(),
            "featured": featured == "on",
            "handmade_hours": handmade_hours,
        },
    )
    return RedirectResponse(url="/admin", status_code=303)


@router.get("/productos/{product_id}/editar")
def edit_product_form(product_id: int, request: Request, db: Session = Depends(get_db)):
    redirect = _require_admin(request)
    if redirect:
        return redirect
    product = get_product(db, product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return templates.TemplateResponse(
        "admin/product_form.html",
        {
            "request": request,
            "title": f"Editar {product.name} — Unika",
            "page": "admin",
            "product": product,
            "form_action": f"/admin/productos/{product.id}",
        },
    )


@router.post("/productos/{product_id}")
def update_product_submit(
    product_id: int,
    request: Request,
    name: str = Form(...),
    category: str = Form(...),
    short_description: str = Form(...),
    description: str = Form(...),
    materials: str = Form(...),
    color: str = Form(...),
    dimensions: str = Form(""),
    price: float = Form(...),
    stock: int = Form(1),
    image: str = Form("/static/img/placeholder.svg"),
    gallery: str = Form(""),
    featured: str = Form(""),
    handmade_hours: int = Form(0),
    db: Session = Depends(get_db),
):
    redirect = _require_admin(request)
    if redirect:
        return redirect
    product = get_product(db, product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    update_product(
        db,
        product,
        {
            "name": name.strip(),
            "category": category.strip().lower(),
            "short_description": short_description.strip(),
            "description": description.strip(),
            "materials": materials.strip(),
            "color": color.strip(),
            "dimensions": dimensions.strip(),
            "price": price,
            "stock": stock,
            "image": image.strip() or "/static/img/placeholder.svg",
            "gallery": gallery.strip(),
            "featured": featured == "on",
            "handmade_hours": handmade_hours,
        },
    )
    return RedirectResponse(url="/admin", status_code=303)


@router.post("/productos/{product_id}/eliminar")
def delete_product_submit(product_id: int, request: Request, db: Session = Depends(get_db)):
    redirect = _require_admin(request)
    if redirect:
        return redirect
    product = get_product(db, product_id)
    if product:
        delete_product(db, product)
    return RedirectResponse(url="/admin", status_code=303)

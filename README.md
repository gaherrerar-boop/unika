# Unika — Tejidos a mano

Sitio web boutique para una marca chilena de **carteras, chalecos y accesorios tejidos a mano**.
Construido con **FastAPI + Jinja2 + SQLAlchemy + SQLite**, sin frameworks de frontend ni CDNs.

---

## Stack

- Python 3.12+
- FastAPI
- Jinja2
- SQLAlchemy 2 + SQLite
- Uvicorn
- HTML5 / CSS3 / JavaScript vanilla

## Estructura

```
/app
  /static
    /css        Estilos propios (sin CDN)
    /js         Scripts vanilla
    /img        Imágenes y SVG decorativos
  /templates    Plantillas Jinja2
  /routes       Routers FastAPI modulares
  /models       Modelos SQLAlchemy
  /services     Lógica de dominio (productos, contacto)
  /database     Motor de base de datos y seed
  /content      Copy de marca + ideas para redes sociales
main.py
requirements.txt
README.md
.env.example
.gitignore
```

## Instalación

```bash
# 1. Clonar / entrar a la carpeta
cd Unika

# 2. Crear y activar entorno virtual
python -m venv .venv
# Windows PowerShell
.venv\Scripts\Activate.ps1
# macOS / Linux
source .venv/bin/activate

# 3. Instalar dependencias
pip install -r requirements.txt

# 4. Variables de entorno
copy .env.example .env       # Windows
# cp .env.example .env       # macOS / Linux

# 5. Ejecutar el servidor
python main.py
```

La aplicación queda disponible en **http://127.0.0.1:8000**.
El dashboard de administración está en **http://127.0.0.1:8000/admin**.

> Credenciales por defecto (cambiar en `.env`): `admin / unika2026`.

La base de datos SQLite se crea automáticamente con productos de ejemplo
la primera vez que se levanta el servidor.

## Páginas

| Ruta | Descripción |
|------|-------------|
| `/` | Home con propuesta de valor y productos destacados |
| `/catalogo` | Catálogo completo (filtrable por categoría) |
| `/producto/{slug}` | Ficha de producto |
| `/hecho-a-mano` | Sección sobre el valor del tejido a mano |
| `/proceso` | Proceso creativo y producción artesanal |
| `/galeria` | Galería visual |
| `/contacto` | Contacto + formulario de consultas / pedidos personalizados |
| `/admin` | Dashboard simple para administrar productos (CRUD) |
| `/redes` | Contenido base sugerido para Instagram, Facebook y TikTok |

## Funcionalidades

- Catálogo dinámico con categorías (carteras, chalecos, accesorios).
- Ficha de producto con galería, descripción, materiales y CTA.
- Formulario de consulta y pedido personalizado.
- Dashboard admin con CRUD básico de productos.
- Contenido editorial para marca artesanal premium.
- Banco de ideas para redes sociales (captions, reels, frases).
- Diseño responsive, paleta neutra y tipografía editorial.

## Mejoras futuras recomendadas

1. **Pasarela de pago** (Webpay / Mercado Pago) para venta directa.
2. **Carrito y checkout** persistente por sesión.
3. **Gestión de imágenes** real desde el admin (subida + recorte).
4. **Autenticación robusta** con `fastapi-users` o JWT.
5. **Multi-idioma** (ES / EN) para alcance internacional.
6. **Blog editorial** con historias de artesanas y procesos.
7. **Integración con Instagram Graph API** para feed automático.
8. **SEO técnico**: sitemap.xml, datos estructurados Product, OG tags dinámicos.
9. **Caché** con Redis y CDN para imágenes en producción.
10. **Tests** con pytest + httpx para rutas y servicios.

---

Hecho con cariño para una marca que cree en lo único, lo lento y lo bien hecho.

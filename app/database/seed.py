"""Datos semilla iniciales para la tienda."""
from app.database.session import SessionLocal
from app.models.product import Product


SEED_PRODUCTS = [
    # ===== CHALECOS / SWEATERS =====
    {
        "slug": "chaleco-arcoiris",
        "name": "Chaleco Arcoíris",
        "category": "chalecos",
        "short_description": "Cardigan tejido a crochet en cuadros de colores vivos: fucsia, rosa, lila y celeste.",
        "description": (
            "Cardigan oversize tejido enteramente a mano en crochet, con un patrón de cuadros "
            "calados que combina fucsia, rosa, lila y celeste. Bordes festoneados, mangas amplias "
            "y caída suelta. Una pieza única, alegre y declarativa, pensada para iluminar un look "
            "neutro o sumarse a una paleta vibrante."
        ),
        "materials": "Hilado de algodón premium teñido a mano",
        "color": "Multicolor (fucsia, rosa, lila, celeste)",
        "dimensions": "Talla única — calza S a L",
        "price": 89990,
        "stock": 2,
        "image": "/static/img/products/chaleco-arcoiris.jpg",
        "gallery": "/static/img/products/chaleco-arcoiris.jpg",
        "featured": True,
        "handmade_hours": 38,
    },
    {
        "slug": "chaleco-noche",
        "name": "Chaleco Noche",
        "category": "chalecos",
        "short_description": "Cardigan oversize en mohair negro, textura suave y caída envolvente.",
        "description": (
            "Cardigan abierto tejido a mano en mohair negro de alta calidad. Punto calado fino "
            "que se siente suave y aireado al tacto, con mangas amplias y largo medio. Pieza "
            "atemporal y elegante, ideal para entretiempo o para sumar drama a un look minimalista."
        ),
        "materials": "Mohair y lana merino",
        "color": "Negro profundo",
        "dimensions": "Talla única — calza S a L",
        "price": 99990,
        "stock": 3,
        "image": "/static/img/products/chaleco-noche.jpg",
        "gallery": "/static/img/products/chaleco-noche.jpg",
        "featured": True,
        "handmade_hours": 42,
    },
    {
        "slug": "sweater-magenta",
        "name": "Sweater Magenta",
        "category": "chalecos",
        "short_description": "Sweater calado en mohair magenta, manga larga y caída fluida.",
        "description": (
            "Sweater cerrado tejido a mano en mohair magenta, con un patrón calado horizontal "
            "que deja entrever la piel. Cuello redondo, mangas largas globo y caída suave. Una "
            "pieza romántica y luminosa, perfecta para capas suaves de entretiempo."
        ),
        "materials": "Mohair 70%, lana merino 30%",
        "color": "Magenta intenso",
        "dimensions": "Talla única — calza S a L",
        "price": 84990,
        "stock": 3,
        "image": "/static/img/products/sweater-magenta.jpg",
        "gallery": "/static/img/products/sweater-magenta.jpg",
        "featured": True,
        "handmade_hours": 30,
    },
    {
        "slug": "chaleco-rosa-lila",
        "name": "Chaleco Rosa & Lila",
        "category": "chalecos",
        "short_description": "Cardigan corto en mohair rosa pastel y lila, con botones de madera.",
        "description": (
            "Cardigan corto cropped, tejido a mano en mohair en degradé de rosa y lila. Cuello en "
            "V, punto calado delicado y botones de madera en el frente. Una prenda dulce y "
            "femenina que se vuelve protagonista de cualquier outfit casual."
        ),
        "materials": "Mohair y lana suave",
        "color": "Rosa pastel y lila",
        "dimensions": "Talla única — calza XS a M",
        "price": 79990,
        "stock": 4,
        "image": "/static/img/products/chaleco-rosa-lila.jpg",
        "gallery": "/static/img/products/chaleco-rosa-lila.jpg",
        "featured": True,
        "handmade_hours": 28,
    },
    {
        "slug": "chaleco-fucsia-borde",
        "name": "Chaleco Fiesta",
        "category": "chalecos",
        "short_description": "Cardigan abierto en jaspeado violeta con bordes y puños fucsia.",
        "description": (
            "Cardigan abierto de cuerpo amplio, tejido a mano en hilado jaspeado en tonos lila y "
            "violeta. Bordes anchos y puños arremangados en fucsia vibrante que enmarcan la pieza. "
            "Caída relajada, ideal para sumar color a jeans claros o blancos."
        ),
        "materials": "Mezcla de algodón y acrílico premium jaspeado",
        "color": "Violeta jaspeado con fucsia",
        "dimensions": "Talla única — calza S a L",
        "price": 82990,
        "stock": 2,
        "image": "/static/img/products/chaleco-fucsia-borde.jpg",
        "gallery": "/static/img/products/chaleco-fucsia-borde.jpg",
        "featured": False,
        "handmade_hours": 32,
    },
    {
        "slug": "chaleco-terracota",
        "name": "Chaleco Terracota",
        "category": "chalecos",
        "short_description": "Cardigan en mohair color terracota, textura esponjosa y abrigada.",
        "description": (
            "Cardigan abierto tejido a mano en mohair color terracota cálido. Punto calado suave, "
            "mangas globo y largo medio. Una prenda envolvente y abrigada, con un tono que "
            "favorece todos los tonos de piel y combina con neutros, jeans y prendas blancas."
        ),
        "materials": "Mohair 80%, lana merino 20%",
        "color": "Terracota / rosa palo",
        "dimensions": "Talla única — calza S a L",
        "price": 87990,
        "stock": 3,
        "image": "/static/img/products/chaleco-terracota.jpg",
        "gallery": "/static/img/products/chaleco-terracota.jpg",
        "featured": True,
        "handmade_hours": 34,
    },
    {
        "slug": "sweater-flores",
        "name": "Sweater Flores",
        "category": "chalecos",
        "short_description": "Sweater crema peludo con flores lila bordadas y cuello en V con encaje.",
        "description": (
            "Sweater cerrado tejido a mano en hilado peludo color crudo, con flores lilas tejidas "
            "en el cuerpo y un cuello en V rematado en encaje crochet. Mangas globo media y caída "
            "relajada. Una pieza romántica con detalle floral, perfecta para días frescos."
        ),
        "materials": "Hilado peludo premium, detalles a crochet",
        "color": "Crudo con flores lila",
        "dimensions": "Talla única — calza S a L",
        "price": 76990,
        "stock": 4,
        "image": "/static/img/products/sweater-flores.jpg",
        "gallery": "/static/img/products/sweater-flores.jpg",
        "featured": False,
        "handmade_hours": 26,
    },

    # ===== CARTERAS =====
    {
        "slug": "cartera-mandala-rosa",
        "name": "Cartera Mandala Rosa",
        "category": "carteras",
        "short_description": "Bandolera redonda tejida a crochet en crudo con flor rosa central.",
        "description": (
            "Bandolera circular tejida a crochet en algodón crudo, con una flor rosa pastel "
            "tejida en relieve al centro y borde festoneado. Forro interno y correa larga "
            "ajustable. Un accesorio dulce y único, ideal para sumar textura a un look de día."
        ),
        "materials": "Algodón peinado, forro de algodón, detalles a crochet",
        "color": "Crudo con flor rosa",
        "dimensions": "24 cm de diámetro x 6 cm de fondo",
        "price": 42990,
        "stock": 4,
        "image": "/static/img/products/cartera-mandala-rosa.jpg",
        "gallery": "/static/img/products/cartera-mandala-rosa.jpg",
        "featured": True,
        "handmade_hours": 14,
    },
    {
        "slug": "cartera-bucket-menta",
        "name": "Cartera Bucket Menta",
        "category": "carteras",
        "short_description": "Bolso bucket tejido en crochet verde menta con dije de madera.",
        "description": (
            "Bolso bucket tejido a crochet en hilado de algodón verde menta. Cierre con cordón "
            "ajustable, dije de madera grabado y correa larga al hombro. Espacio amplio en su "
            "interior. Una pieza fresca y versátil para acompañar el día a día."
        ),
        "materials": "Algodón mercerizado, dije de madera",
        "color": "Verde menta",
        "dimensions": "26 cm x 22 cm x 12 cm",
        "price": 46990,
        "stock": 3,
        "image": "/static/img/products/cartera-bucket-menta.jpg",
        "gallery": "/static/img/products/cartera-bucket-menta.jpg",
        "featured": True,
        "handmade_hours": 16,
    },
    {
        "slug": "cartera-bucket-crudo",
        "name": "Cartera Bucket Crudo",
        "category": "carteras",
        "short_description": "Bolso bucket en crochet calado color crudo con dije de madera firmado.",
        "description": (
            "Bolso bucket tejido a crochet en hilado de algodón crudo, con patrón calado "
            "geométrico y cierre con cordón. Dije de madera firmado Unika y correa larga. "
            "Una cartera atemporal en tono neutro, perfecta para combinar con todo."
        ),
        "materials": "Algodón mercerizado, dije de madera",
        "color": "Crudo natural",
        "dimensions": "26 cm x 24 cm x 12 cm",
        "price": 46990,
        "stock": 4,
        "image": "/static/img/products/cartera-bucket-crudo.jpg",
        "gallery": "/static/img/products/cartera-bucket-crudo.jpg",
        "featured": False,
        "handmade_hours": 16,
    },
    {
        "slug": "cartera-rosa-dorada",
        "name": "Cartera Joya Rosa",
        "category": "carteras",
        "short_description": "Cartera de mano rosa con asa metálica dorada y flor crochet.",
        "description": (
            "Cartera de mano tejida a crochet en rosa pastel, con cuerpo texturado de pompones y "
            "flor central en relieve. Asa rígida en metal dorado y dije de madera firmado Unika. "
            "Una pieza joya, ideal para eventos, cocktails o sumar carácter a un look sencillo."
        ),
        "materials": "Hilado de algodón, asa metálica dorada, madera",
        "color": "Rosa pastel",
        "dimensions": "24 cm x 20 cm x 8 cm",
        "price": 52990,
        "stock": 2,
        "image": "/static/img/products/cartera-rosa-dorada.jpg",
        "gallery": "/static/img/products/cartera-rosa-dorada.jpg",
        "featured": True,
        "handmade_hours": 18,
    },
    {
        "slug": "cartera-crudo-cuero",
        "name": "Cartera Volantes",
        "category": "carteras",
        "short_description": "Cartera de mano con volantes en crochet crudo y asa de cuero rojo.",
        "description": (
            "Cartera de mano de silueta romántica, tejida a crochet en algodón crudo con "
            "volantes que enmarcan la apertura. Asa rígida forrada en cuero rojo curtido y "
            "dije de madera. Pieza expresiva y femenina, ideal para destacar."
        ),
        "materials": "Algodón mercerizado, cuero rojo, madera",
        "color": "Crudo con asa roja",
        "dimensions": "28 cm x 18 cm x 8 cm",
        "price": 54990,
        "stock": 2,
        "image": "/static/img/products/cartera-crudo-cuero.jpg",
        "gallery": "/static/img/products/cartera-crudo-cuero.jpg",
        "featured": False,
        "handmade_hours": 20,
    },
    {
        "slug": "cartera-redonda-rosa",
        "name": "Cartera Luna Rosa",
        "category": "carteras",
        "short_description": "Bandolera redonda en crochet rosa palo con correa de cuero.",
        "description": (
            "Bandolera circular tejida a crochet en algodón rosa palo, con patrón en estrella "
            "calada y correa larga de cuero curtido. Cierre cremallera y dije de madera firmado "
            "Unika. Una cartera elegante y minimalista, perfecta para todos los días."
        ),
        "materials": "Algodón mercerizado, correa de cuero, madera",
        "color": "Rosa palo",
        "dimensions": "22 cm de diámetro x 6 cm de fondo",
        "price": 44990,
        "stock": 3,
        "image": "/static/img/products/cartera-redonda-rosa.jpg",
        "gallery": "/static/img/products/cartera-redonda-rosa.jpg",
        "featured": True,
        "handmade_hours": 14,
    },
    {
        "slug": "cartera-rosa-bambu",
        "name": "Cartera Bambú Rosa",
        "category": "carteras",
        "short_description": "Cartera de mano en crochet rosa palo con asas de bambú natural.",
        "description": (
            "Cartera de mano de silueta clásica, tejida a crochet en hilado rosa palo con "
            "perlas tejidas en el cuerpo. Asas curvas de bambú natural y dije firmado Unika. "
            "Una pieza versátil que conjuga lo artesanal con un toque vintage."
        ),
        "materials": "Algodón mercerizado, bambú natural",
        "color": "Rosa palo",
        "dimensions": "30 cm x 18 cm x 10 cm",
        "price": 49990,
        "stock": 3,
        "image": "/static/img/products/cartera-rosa-bambu.jpg",
        "gallery": "/static/img/products/cartera-rosa-bambu.jpg",
        "featured": False,
        "handmade_hours": 18,
    },
    {
        "slug": "cartera-redonda-azul",
        "name": "Cartera Noche Azul",
        "category": "carteras",
        "short_description": "Cartera redonda en crochet azul noche con asas de madera tinte cerezo.",
        "description": (
            "Cartera de mano circular tejida a crochet en algodón azul noche, con efecto rosetón "
            "en relieve. Asas redondas de madera teñida color cereza y dije firmado Unika. Pieza "
            "sofisticada que aporta carácter a looks neutros y de noche."
        ),
        "materials": "Algodón mercerizado, madera teñida",
        "color": "Azul noche",
        "dimensions": "26 cm de diámetro x 8 cm de fondo",
        "price": 52990,
        "stock": 2,
        "image": "/static/img/products/cartera-redonda-azul.jpg",
        "gallery": "/static/img/products/cartera-redonda-azul.jpg",
        "featured": True,
        "handmade_hours": 20,
    },
    {
        "slug": "cartera-crudo-madera",
        "name": "Cartera Ondas",
        "category": "carteras",
        "short_description": "Cartera de mano en crochet crudo con flecos y asas de madera.",
        "description": (
            "Cartera de mano de silueta media luna, tejida a crochet en algodón crudo con "
            "flecos suaves en la base. Asas curvas de madera natural y dije firmado Unika. "
            "Una pieza con movimiento y textura, ideal para días de sol y looks relajados."
        ),
        "materials": "Algodón mercerizado, madera natural",
        "color": "Crudo natural",
        "dimensions": "32 cm x 22 cm x 10 cm",
        "price": 54990,
        "stock": 2,
        "image": "/static/img/products/cartera-crudo-madera.jpg",
        "gallery": "/static/img/products/cartera-crudo-madera.jpg",
        "featured": False,
        "handmade_hours": 22,
    },
    {
        "slug": "cartera-perlas-crudo",
        "name": "Cartera Perlas",
        "category": "carteras",
        "short_description": "Bandolera en crochet crudo con correa de perlas tejidas y dije firmado.",
        "description": (
            "Bandolera tejida a crochet en algodón crudo, con patrón de círculos en relieve y "
            "correa elaborada con perlas tejidas a mano. Dije de madera firmado Unika. Una pieza "
            "delicada y distintiva, pensada para acompañar looks femeninos durante todo el año."
        ),
        "materials": "Algodón mercerizado, perlas tejidas, madera",
        "color": "Crudo natural",
        "dimensions": "28 cm x 18 cm x 6 cm",
        "price": 56990,
        "stock": 3,
        "image": "/static/img/products/cartera-perlas-crudo.jpg",
        "gallery": "/static/img/products/cartera-perlas-crudo.jpg",
        "featured": True,
        "handmade_hours": 24,
    },
    {
        "slug": "cartera-circulos-crudo",
        "name": "Cartera Círculos",
        "category": "carteras",
        "short_description": "Bandolera en crochet crudo con motivo circular y correa de perlas.",
        "description": (
            "Bandolera tejida a crochet en algodón crudo, formada por círculos calados unidos a "
            "mano y rematados con perlas tejidas en la correa. Cierre cremallera y dije firmado "
            "Unika. Una pieza luminosa, ideal para días claros y looks relajados."
        ),
        "materials": "Algodón mercerizado, perlas tejidas, madera",
        "color": "Crudo natural",
        "dimensions": "28 cm x 18 cm x 6 cm",
        "price": 56990,
        "stock": 3,
        "image": "/static/img/products/cartera-circulos-crudo.jpg",
        "gallery": "/static/img/products/cartera-circulos-crudo.jpg",
        "featured": False,
        "handmade_hours": 24,
    },
]


def seed_products() -> None:
    """Inserta productos de ejemplo si la tabla está vacía."""
    db = SessionLocal()
    try:
        if db.query(Product).count() > 0:
            return
        for data in SEED_PRODUCTS:
            db.add(Product(**data))
        db.commit()
    finally:
        db.close()

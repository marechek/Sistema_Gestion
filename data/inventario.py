# Simulación de base de datos en memoria

# Tupla
CATEGORIAS = ("Alimentos", "Juguetes", "Higiene", "Accesorios")

# Lista
inventario = [
    {
        "id": 1,
        "nombre": "Alimento Premium Perro 15kg",
        "categoria": "Alimentos",
        "precio": 45990,
        "stock": 12,
        "stock_minimo": 5,
        "activo": True
    },
    {
        "id": 2,
        "nombre": "Alimento Gato Adulto 8kg",
        "categoria": "Alimentos",
        "precio": 32990,
        "stock": 3,
        "stock_minimo": 5,
        "activo": True
    },
    {
        "id": 3,
        "nombre": "Pelota de Goma Resistente",
        "categoria": "Juguetes",
        "precio": 5990,
        "stock": 25,
        "stock_minimo": 10,
        "activo": True
    },
    {
        "id": 4,
        "nombre": "Rascador para Gatos",
        "categoria": "Accesorios",
        "precio": 21990,
        "stock": 0,
        "stock_minimo": 2,
        "activo": False
    },
    {
        "id": 5,
        "nombre": "Shampoo Hipoalergénico Mascotas",
        "categoria": "Higiene",
        "precio": 8990,
        "stock": 18,
        "stock_minimo": 5,
        "activo": True
    }
]

# Set
ids_productos = {producto["id"] for producto in inventario}

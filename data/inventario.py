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
        "stock": 12
    },
    {
        "id": 2,
        "nombre": "Alimento Gato Adulto 8kg",
        "categoria": "Alimentos",
        "precio": 32990,
        "stock": 8
    },
    {
        "id": 3,
        "nombre": "Pelota de Goma Resistente",
        "categoria": "Juguetes",
        "precio": 5990,
        "stock": 25
    },
    {
        "id": 4,
        "nombre": "Rascador para Gatos",
        "categoria": "Accesorios",
        "precio": 21990,
        "stock": 5
    },
    {
        "id": 5,
        "nombre": "Shampoo Hipoalergénico Mascotas",
        "categoria": "Higiene",
        "precio": 8990,
        "stock": 18
    }
]

# Set
ids_productos = {producto["id"] for producto in inventario}

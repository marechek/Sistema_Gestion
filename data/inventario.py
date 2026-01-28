CATEGORIAS = {
    1: "Alimentos",
    2: "Juguetes",
    3: "Higiene",
    4: "Accesorios"
}

inventario = [
    {
        "id": 1,
        "nombre": "Alimento Premium Perro 15kg",
        "categoria_id": 1,
        "precio": 45990,
        "stock": 12,
        "stock_minimo": 5,
        "activo": True
    },
    {
        "id": 2,
        "nombre": "Alimento Gato Adulto 8kg",
        "categoria_id": 1,
        "precio": 32990,
        "stock": 3,
        "stock_minimo": 5,
        "activo": True
    },
    {
        "id": 3,
        "nombre": "Pelota de Goma Resistente",
        "categoria_id": 2,
        "precio": 5990,
        "stock": 25,
        "stock_minimo": 10,
        "activo": True
    },
    {
        "id": 4,
        "nombre": "Rascador para Gatos",
        "categoria_id": 4,
        "precio": 21990,
        "stock": 0,
        "stock_minimo": 2,
        "activo": False
    },
    {
        "id": 5,
        "nombre": "Shampoo Hipoalergénico Mascotas",
        "categoria_id": 3,
        "precio": 8990,
        "stock": 18,
        "stock_minimo": 5,
        "activo": True
    }
]

ids_productos = {producto["id"] for producto in inventario}

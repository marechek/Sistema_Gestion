# Lógica de negocio del módulo Inventario

from data.inventario import inventario, ids_productos, CATEGORIAS
from utils.validaciones import (
    validar_entero,
    validar_flotante,
    validar_texto_no_vacio
)


def mostrar_categorias():
    print("\nCategorías disponibles:")
    for categoria in CATEGORIAS:
        print(f"- {categoria}")


def listar_productos():
    if not inventario:
        print("\nInventario vacío.")
        return

    print("\nLISTADO DE PRODUCTOS")
    print("-" * 60)
    for producto in inventario:
        print(
            f"ID: {producto['id']} | "
            f"{producto['nombre']} | "
            f"Categoría: {producto['categoria']} | "
            f"Precio: ${producto['precio']:,} | "
            f"Stock: {producto['stock']}"
        )
    print("-" * 60)


def agregar_producto():
    print("\nAGREGAR PRODUCTO")

    id_producto = validar_entero("ID del producto: ")
    if id_producto in ids_productos:
        print("El ID ya existe. Operación cancelada.")
        return

    nombre = validar_texto_no_vacio("Nombre del producto: ")

    mostrar_categorias()
    categoria = validar_texto_no_vacio("Categoría: ")
    if categoria not in CATEGORIAS:
        print("Categoría inválida.")
        return

    precio = validar_flotante("Precio: ")
    stock = validar_entero("Stock inicial: ")

    producto = {
        "id": id_producto,
        "nombre": nombre,
        "categoria": categoria,
        "precio": precio,
        "stock": stock
    }

    inventario.append(producto)
    ids_productos.add(id_producto)

    print("Producto agregado correctamente.")


def buscar_producto_por_id(id_producto):
    for producto in inventario:
        if producto["id"] == id_producto:
            return producto
    return None


def actualizar_stock():
    print("\nACTUALIZAR STOCK")

    id_producto = validar_entero("ID del producto: ")
    producto = buscar_producto_por_id(id_producto)

    if not producto:
        print("Producto no encontrado.")
        return

    nuevo_stock = validar_entero("Nuevo stock: ")
    producto["stock"] = nuevo_stock

    print("Stock actualizado correctamente.")


def eliminar_producto():
    print("\nELIMINAR PRODUCTO")

    id_producto = validar_entero("ID del producto: ")
    producto = buscar_producto_por_id(id_producto)

    if not producto:
        print("Producto no encontrado.")
        return

    inventario.remove(producto)
    ids_productos.remove(id_producto)

    print("Producto eliminado del inventario.")

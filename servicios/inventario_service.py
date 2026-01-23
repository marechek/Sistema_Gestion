# Lógica de negocio del módulo Inventario

from data.inventario import inventario, ids_productos, CATEGORIAS
from utils.validaciones import (
    validar_entero,
    validar_flotante,
    validar_texto_no_vacio,
    formato_pesos_clp
)

def generar_id_producto(id_actual=1):
    """
    Genera un ID único para un producto usando recursividad.
    """
    if id_actual not in ids_productos:
        return id_actual
    return generar_id_producto(id_actual + 1)


def mostrar_categorias():
    print("\nCategorías disponibles:")
    for categoria in CATEGORIAS:
        print(f"- {categoria}")


def listar_productos():
    if not inventario:
        print("\nInventario vacío.")
        return

    print("\nLISTADO DE PRODUCTOS")
    print("-" * 110)

    for producto in inventario:
        precio = formato_pesos_clp(producto["precio"])
        estado = "Activo" if producto["activo"] else "Inactivo"
        alerta_stock = " STOCK BAJO" if producto["stock"] <= producto["stock_minimo"] else ""

        print(
            f"ID: {producto['id']} | "
            f"{producto['nombre']} | "
            f"Cat: {producto['categoria']} | "
            f"Precio: ${precio} | "
            f"Stock: {producto['stock']} | "
            f"Mín: {producto['stock_minimo']} | "
            f"Estado: {estado}{alerta_stock}"
        )

    print("-" * 110)


def agregar_producto():
    print("\nAGREGAR PRODUCTO")

    id_producto = generar_id_producto()
    print(f"ID asignado automáticamente: {id_producto}")

    nombre = validar_texto_no_vacio("Nombre del producto: ")

    mostrar_categorias()
    categoria = validar_texto_no_vacio("Categoría: ")
    if categoria not in CATEGORIAS:
        print("Categoría inválida.")
        return

    precio = validar_flotante("Precio: ")
    stock = validar_entero("Stock inicial: ")
    stock_minimo = validar_entero("Stock mínimo: ")

    producto = {
        "id": id_producto,
        "nombre": nombre,
        "categoria": categoria,
        "precio": precio,
        "stock": stock,
        "stock_minimo": stock_minimo,
        "activo": True
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
    print("\n DESACTIVAR PRODUCTO")

    id_producto = validar_entero("ID del producto: ")
    producto = buscar_producto_por_id(id_producto)

    if not producto:
        print("Producto no encontrado.")
        return

    producto["activo"] = False
    print("Producto desactivado correctamente.")


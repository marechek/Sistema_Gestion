# Lógica de negocio del módulo Inventario

from data.inventario import inventario, CATEGORIAS
from utils.validaciones import (
    validar_entero,
    validar_flotante,
    validar_texto_no_vacio,
    formato_pesos_clp
)

def obtener_ids_existentes():
    return {producto["id"] for producto in inventario}

def generar_id_producto(id_actual=1):
    """
    Genera un ID único para un producto usando recursividad.
    """
    ids_existentes = obtener_ids_existentes()

    if id_actual not in ids_existentes:
        return id_actual

    return generar_id_producto(id_actual + 1)


def mostrar_categorias():
    print("\nCategorías disponibles:")
    for id_cat, nombre in CATEGORIAS.items():
        print(f"{id_cat}. {nombre}")

def obtener_categoria_id():
    """
    Permite seleccionar una categoría por ID o por nombre.
    Repite hasta que la categoría sea válida.
    """
    while True:
        mostrar_categorias()
        entrada = input("Seleccione categoría (ID o nombre): ").strip()

        if entrada.isdigit():
            id_cat = int(entrada)
            if id_cat in CATEGORIAS:
                return id_cat
            print("ID de categoría inválido.")
            continue

        for id_cat, nombre in CATEGORIAS.items():
            if entrada.lower() == nombre.lower():
                return id_cat

        print("Categoría no encontrada. Intente nuevamente.")

def mostrar_producto(producto):
    precio = formato_pesos_clp(producto["precio"])
    estado = "Activo" if producto["activo"] else "Inactivo"
    alerta_stock = " ⚠ STOCK BAJO" if producto["stock"] <= producto["stock_minimo"] else ""
    categoria = CATEGORIAS.get(producto["categoria_id"], "N/A")

    print(
        f"ID: {producto['id']} | "
        f"{producto['nombre']} | "
        f"Cat: {categoria} | "
        f"Precio: ${precio} | "
        f"Stock: {producto['stock']} | "
        f"Mín: {producto['stock_minimo']} | "
        f"Estado: {estado}{alerta_stock}"
    )


def listar_productos():
    if not inventario:
        print("\nInventario vacío.")
        return

    print("\nLISTADO DE PRODUCTOS")
    print("-" * 110)

    for producto in inventario:
        mostrar_producto(producto)

    print("-" * 110)


def agregar_producto():
    print("\nAGREGAR PRODUCTO")

    id_producto = generar_id_producto()
    print(f"ID asignado automáticamente: {id_producto}")

    nombre = validar_texto_no_vacio("Nombre del producto: ")
    categoria_id = obtener_categoria_id()
    precio = validar_flotante("Precio: ")
    stock = validar_entero("Stock inicial: ")
    stock_minimo = validar_entero("Stock mínimo: ")

    producto = {
        "id": id_producto,
        "nombre": nombre,
        "categoria_id": categoria_id,
        "precio": precio,
        "stock": stock,
        "stock_minimo": stock_minimo,
        "activo": True
    }

    inventario.append(producto)

    print("Producto agregado correctamente.")
    mostrar_producto(producto)


def buscar_producto_por_id(id_producto):
    for producto in inventario:
        if producto["id"] == id_producto:
            return producto
    return None


def actualizar_stock():
    print("\nACTUALIZAR STOCK")
    listar_productos()

    id_producto = validar_entero("ID del producto: ")
    producto = buscar_producto_por_id(id_producto)

    if not producto:
        print("Producto no encontrado.")
        return

    producto["stock"] = validar_entero("Nuevo stock: ")
    print("Stock actualizado correctamente.")
    mostrar_producto(producto)


def activar_producto():
    print("\nACTIVAR PRODUCTO")
    listar_productos()

    id_producto = validar_entero("ID del producto: ")
    producto = buscar_producto_por_id(id_producto)

    if not producto:
        print("Producto no encontrado.")
        return
    if producto["activo"]:
        print("El producto seleccionado ya está activo. No se realizó ningún cambio.")
        return

    producto["activo"] = True
    print("Producto activado correctamente.")
    mostrar_producto(producto)


def desactivar_producto():
    print("\nDESACTIVAR PRODUCTO")
    listar_productos()

    id_producto = validar_entero("ID del producto: ")
    producto = buscar_producto_por_id(id_producto)

    if not producto:
        print("Producto no encontrado.")
        return
    if not producto["activo"]:
        print("El producto seleccionado ya está inactivo. No se realizó ningún cambio.")
        return

    producto["activo"] = False
    print("Producto desactivado correctamente.")
    mostrar_producto(producto)


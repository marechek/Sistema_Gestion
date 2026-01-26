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
    for i, categoria in enumerate(CATEGORIAS, start=1):
        print(f"{i}. {categoria}")

def obtener_categoria():
    """
    Permite seleccionar una categoría por ID o por nombre.
    Repite hasta que la categoría sea válida.
    """
    while True:
        mostrar_categorias()
        entrada = input("Seleccione categoría (ID o nombre): ").strip()

        # Intento por ID
        if entrada.isdigit():
            indice = int(entrada) - 1
            if 0 <= indice < len(CATEGORIAS):
                return CATEGORIAS[indice]
            else:
                print("ID de categoría inválido.")
                continue

        # Intento por nombre
        for categoria in CATEGORIAS:
            if entrada.lower() == categoria.lower():
                return categoria

        print("Categoría no encontrada. Intente nuevamente.")

def mostrar_producto(producto):
    precio = formato_pesos_clp(producto["precio"])
    estado = "Activo" if producto["activo"] else "Inactivo"
    alerta_stock = " STOCK BAJO" if producto["stock"] <= producto["stock_minimo"] else ""

    salida = (
        f"ID: {producto['id']} | "
        f"{producto['nombre']} | "
        f"Cat: {producto['categoria']} | "
        f"Precio: ${precio} | "
        f"Stock: {producto['stock']} | "
        f"Mín: {producto['stock_minimo']} | "
        f"Estado: {estado}{alerta_stock}"
    )

    print(salida)


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

    categoria = obtener_categoria()

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

    listar_productos()

    id_producto = validar_entero("ID del producto: ")
    producto = buscar_producto_por_id(id_producto)

    if not producto:
        print("Producto no encontrado.")
        return

    nuevo_stock = validar_entero("Nuevo stock: ")
    producto["stock"] = nuevo_stock

    print("Stock actualizado correctamente.")
    print("Producto actualizado:")
    mostrar_producto(producto)


def desactivar_producto():
    print("\n DESACTIVAR PRODUCTO")

    listar_productos()

    id_producto = validar_entero("ID del producto: ")
    producto = buscar_producto_por_id(id_producto)

    if not producto:
        print("Producto no encontrado.")
        return
    elif not producto["activo"]:
        print("El producto seleccionado ya está inactivo. No se realiza ninguna acción.")
        return

    producto["activo"] = False
    print("Producto desactivado correctamente.")
    mostrar_producto(producto)

def activar_producto():
    print("\n ACTIVAR PRODUCTO")

    listar_productos()

    id_producto = validar_entero("ID del producto: ")
    producto = buscar_producto_por_id(id_producto)

    if not producto:
        print("Producto no encontrado.")
        return
    elif producto["activo"]:
        print("El producto seleccionado ya está activo. No se realiza ninguna acción.")
        return
    
    producto["activo"] = True
    print("Producto activado correctamente.")
    mostrar_producto(producto)


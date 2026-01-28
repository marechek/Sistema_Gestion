# Lógica de negocio del módulo Ventas

from data.ventas import ventas
from data.inventario import inventario
from data.clientes import clientes

from utils.validaciones import validar_entero, formato_pesos_clp

from servicios.inventario_service import listar_productos, buscar_producto_por_id, mostrar_producto
from servicios.clientes_service import listar_clientes, buscar_cliente_por_id, mostrar_cliente


def obtener_ids_ventas_existentes():
    return {venta["id"] for venta in ventas}


def generar_id_venta(id_actual=1):
    """
    Genera un ID único para una venta.
    """
    ids_existentes = obtener_ids_ventas_existentes()

    if id_actual not in ids_existentes:
        return id_actual

    return generar_id_venta(id_actual + 1)


def obtener_cantidad_en_carrito(carrito, id_producto):
    """
    Suma cuántas unidades del producto ya están en el carrito
    (para no pasarse del stock disponible).
    """
    total = 0
    for item in carrito:
        if item["producto_id"] == id_producto:
            total += item["cantidad"]
    return total


def calcular_total_recursivo(items, index=0):
    """
    Calcula el total de la venta.
    """
    if index >= len(items):
        return 0

    return items[index]["subtotal"] + calcular_total_recursivo(items, index + 1)


def crear_venta():
    print("\nCREAR VENTA")

    print("\nSeleccione un cliente:")
    listar_clientes()

    id_cliente = validar_entero("ID del cliente: ")
    cliente = buscar_cliente_por_id(id_cliente)

    if not cliente:
        print("Cliente no encontrado.")
        return

    if not cliente["activo"]:
        print("El cliente está inactivo. No se puede generar una venta.")
        return

    print("\nCliente seleccionado:")
    mostrar_cliente(cliente)

    # Construir carrito.
    carrito = []

    def mostrar_menu_carrito(opciones):
        print("\n--- CARRITO DE COMPRA ---")
        for key, valor in opciones.items():
            print(f"{key}. {valor[0]}")

    def accion_agregar_producto():
        print("\nSeleccione un producto:")
        listar_productos()

        id_producto = validar_entero("ID del producto: ")
        producto = buscar_producto_por_id(id_producto)

        if not producto:
            print("Producto no encontrado.")
            return

        if not producto["activo"]:
            print("El producto está inactivo. No se puede vender.")
            return

        ya_en_carrito = obtener_cantidad_en_carrito(carrito, id_producto)
        stock_disponible = producto["stock"] - ya_en_carrito

        if stock_disponible <= 0:
            print("No hay stock disponible para este producto.")
            return

        print("\nProducto seleccionado:")
        mostrar_producto(producto)
        print(f"Stock disponible para esta venta: {stock_disponible}")

        cantidad = validar_entero("Cantidad: ")

        if cantidad <= 0:
            print("La cantidad debe ser mayor a 0.")
            return

        if cantidad > stock_disponible:
            print("Cantidad supera el stock disponible para esta venta.")
            return

        item = {
            "producto_id": producto["id"],
            "nombre": producto["nombre"],
            "precio": producto["precio"],
            "cantidad": cantidad,
            "subtotal": producto["precio"] * cantidad
        }

        carrito.append(item)
        print("Producto agregado al carrito.")

    def accion_ver_carrito():
        if not carrito:
            print("\nCarrito vacío.")
            return

        print("\nDETALLE CARRITO")
        print("-" * 110)

        for item in carrito:
            precio = formato_pesos_clp(item["precio"])
            subtotal = formato_pesos_clp(item["subtotal"])
            print(
                f"ID: {item['producto_id']} | "
                f"{item['nombre']} | "
                f"Precio: ${precio} | "
                f"Cantidad: {item['cantidad']} | "
                f"Subtotal: ${subtotal}"
            )

        total = calcular_total_recursivo(carrito)
        print("-" * 110)
        print(f"TOTAL: ${formato_pesos_clp(total)}")

    def accion_finalizar_venta():
        if not carrito:
            print("No puedes finalizar una venta con el carrito vacío.")
            return

        total = calcular_total_recursivo(carrito)
        print(f"\nTotal venta: ${formato_pesos_clp(total)}")
        confirmacion = input("¿Confirmar venta? (s/n): ").lower().strip()

        if confirmacion != "s":
            print("Venta no confirmada.")
            return

        # Actualizo el stock
        for item in carrito:
            producto = buscar_producto_por_id(item["producto_id"])
            if producto:
                producto["stock"] -= item["cantidad"]

        # Registro la venta
        venta = {
            "id": generar_id_venta(),
            "cliente_id": cliente["id"],
            "cliente_nombre": cliente["nombre"],
            "items": carrito,
            "total": total,
            "activo": True
        }

        ventas.append(venta)

        print("\nVenta registrada correctamente.")
        print(
            f"ID Venta: {venta['id']} | "
            f"Cliente: {venta['cliente_nombre']} | "
            f"Total: ${formato_pesos_clp(venta['total'])}"
        )

        return True

    opciones_carrito = {
        "1": ("Agregar producto", accion_agregar_producto),
        "2": ("Ver carrito", accion_ver_carrito),
        "3": ("Finalizar venta", accion_finalizar_venta),
        "0": ("Cancelar", None)
    }

    while True:
        mostrar_menu_carrito(opciones_carrito)
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "0":
            print("Venta cancelada.")
            return

        if opcion not in opciones_carrito:
            print("Opción inválida. Intente nuevamente.")
            continue

        accion = opciones_carrito[opcion][1]

        try:
            resultado = accion()
            if opcion == "3" and resultado is True:
                return
        except Exception as e:
            print("Ocurrió un error al ejecutar la opción.")
            print(f"Detalle técnico: {e}")


def buscar_venta_por_id(id_venta):
    for venta in ventas:
        if venta["id"] == id_venta:
            return venta
    return None


def mostrar_venta(venta, mostrar_detalle=True):
    estado = "Activa" if venta.get("activo", True) else "Anulada"
    total = formato_pesos_clp(venta.get("total", 0))

    print(
        f"ID Venta: {venta['id']} | "
        f"Cliente: {venta.get('cliente_nombre', 'N/A')} | "
        f"Total: ${total} | "
        f"Estado: {estado}"
    )

    if not mostrar_detalle:
        return

    items = venta.get("items", [])
    if not items:
        print("  (Sin items)")
        return

    print("  Detalle:")
    for item in items:
        precio = formato_pesos_clp(item["precio"])
        subtotal = formato_pesos_clp(item["subtotal"])
        print(
            f"  - ID Prod: {item['producto_id']} | "
            f"{item['nombre']} | "
            f"Precio: ${precio} | "
            f"Cantidad: {item['cantidad']} | "
            f"Subtotal: ${subtotal}"
        )


def listar_ventas():
    if not ventas:
        print("\nNo hay ventas registradas.")
        return

    print("\nLISTADO DE VENTAS")
    print("-" * 110)

    for venta in ventas:
        # listado resumido (sin detalle)
        mostrar_venta(venta, mostrar_detalle=False)

    print("-" * 110)


def ver_detalle_venta():
    print("\nVER DETALLE DE VENTA")
    listar_ventas()

    id_venta = validar_entero("ID de la venta: ")
    venta = buscar_venta_por_id(id_venta)

    if not venta:
        print("Venta no encontrada.")
        return

    print("\nDETALLE DE VENTA")
    print("-" * 110)
    mostrar_venta(venta, mostrar_detalle=True)
    print("-" * 110)


def anular_venta():
    print("\nANULAR VENTA")
    listar_ventas()

    id_venta = validar_entero("ID de la venta a anular: ")
    venta = buscar_venta_por_id(id_venta)

    if not venta:
        print("Venta no encontrada.")
        return

    if not venta.get("activo", True):
        print("La venta ya está anulada. No se realizó ningún cambio.")
        return

    confirmacion = input("¿Confirmar anulación? (s/n): ").lower().strip()
    if confirmacion != "s":
        print("Operación cancelada.")
        return

    venta["activo"] = False

    print("Venta anulada correctamente.")
    mostrar_venta(venta, mostrar_detalle=False)



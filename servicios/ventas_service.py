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

    def previsualizar_carrito(carrito):
        """
        Muestra una vista rápida del carrito (items + total).
        Se usa después de agregar productos para mejorar UX.
        """
        if not carrito:
            print("\nCarrito vacío.")
            return

        print("\nPrevisualización del carrito")
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
        print(f"TOTAL PARCIAL: ${formato_pesos_clp(total)}")

    def editar_cantidad_item(carrito, indice, nueva_cantidad):
        """
        Ajusta la cantidad de un item del carrito y sincroniza stock reservado.

        - Si aumenta cantidad: requiere stock disponible en inventario.
        (se descuenta más stock)
        - Si disminuye cantidad: se devuelve stock.
        - Si nueva_cantidad <= 0: no se permite (usar eliminar item).
        Retorna (True/False, mensaje)
        """
        if indice < 0 or indice >= len(carrito):
            return False, "Índice inválido."

        if nueva_cantidad <= 0:
            return False, "Cantidad inválida. Para quitar el producto usa 'Eliminar item'."

        item = carrito[indice]
        producto = buscar_producto_por_id(item["producto_id"])

        if not producto:
            return False, "Producto no encontrado en inventario."

        cantidad_actual = item["cantidad"]
        diferencia = nueva_cantidad - cantidad_actual

        # Si aumenta, necesitamos stock disponible para reservar
        if diferencia > 0:
            if diferencia > producto["stock"]:
                return False, "No hay stock suficiente para aumentar la cantidad."
            producto["stock"] -= diferencia  # reserva adicional

        # Si disminuye, devolvemos stock
        elif diferencia < 0:
            producto["stock"] += abs(diferencia)

        # Actualizar item
        item["cantidad"] = nueva_cantidad
        item["subtotal"] = item["precio"] * nueva_cantidad

        return True, "Cantidad actualizada y stock ajustado."

    
    def eliminar_item_por_indice(carrito, indice):
        """
        Elimina un item del carrito por índice y devuelve el stock reservado.
        Retorna True si eliminó, False si el índice no es válido.
        """
        if indice < 0 or indice >= len(carrito):
            return False

        item = carrito.pop(indice)
        producto = buscar_producto_por_id(item["producto_id"])
        if producto:
            producto["stock"] += item["cantidad"]

        return True

    def devolver_reserva_stock(carrito):
        """
        Devuelve al inventario el stock reservado por los items del carrito.
        Se usa si la venta se cancela o no se confirma.
        """
        for item in carrito:
            producto = buscar_producto_por_id(item["producto_id"])
            if producto:
                producto["stock"] += item["cantidad"]

    def buscar_indice_item_en_carrito(carrito, producto_id):
        """
        Retorna el índice del item en el carrito para ese producto_id,
        o -1 si no existe.
        """
        for i, item in enumerate(carrito):
            if item["producto_id"] == producto_id:
                return i
        return -1
    
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

        if producto["stock"] <= 0:
            print("No hay stock disponible para este producto.")
            return

        print("\nProducto seleccionado:")
        mostrar_producto(producto)

        cantidad = validar_entero("Cantidad: ")

        if cantidad <= 0:
            print("La cantidad debe ser mayor a 0.")
            return

        # RESERVA: se descuenta stock al agregar al carrito
        if cantidad > producto["stock"]:
            print("Cantidad supera el stock disponible.")
            return

        producto["stock"] -= cantidad

        indice = buscar_indice_item_en_carrito(carrito, producto["id"])

        if indice == -1:
            item = {
                "producto_id": producto["id"],
                "nombre": producto["nombre"],
                "precio": producto["precio"],
                "cantidad": cantidad,
                "subtotal": producto["precio"] * cantidad
            }
            carrito.append(item)
            print("Producto agregado al carrito (stock reservado).")
        else:
            carrito[indice]["cantidad"] += cantidad
            carrito[indice]["subtotal"] = carrito[indice]["precio"] * carrito[indice]["cantidad"]
            print("Producto ya estaba en el carrito: cantidad actualizada (stock reservado).")

        try:
            previsualizar_carrito(carrito)
        except NameError:
            pass


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

    def accion_editar_cantidad_item():
        if not carrito:
            print("\nCarrito vacío. No hay nada que editar.")
            return

        print("\nItems en carrito:")
        print("-" * 110)
        for i, item in enumerate(carrito, start=1):
            subtotal = formato_pesos_clp(item["subtotal"])
            print(f"{i}. {item['nombre']} | Cant: {item['cantidad']} | Subtotal: ${subtotal}")
        print("-" * 110)

        nro = validar_entero("Ingrese el número del item a editar: ")
        indice = nro - 1

        if indice < 0 or indice >= len(carrito):
            print("Número inválido.")
            return

        actual = carrito[indice]["cantidad"]
        print(f"Cantidad actual: {actual}")

        nueva = validar_entero("Nueva cantidad: ")

        ok, msg = editar_cantidad_item(carrito, indice, nueva)
        print(msg)

        if ok:
            try:
                previsualizar_carrito(carrito)
            except NameError:
                pass

    
    def accion_eliminar_item():
        if not carrito:
            print("\nCarrito vacío. No hay nada para eliminar.")
            return

        print("\nItems en carrito:")
        print("-" * 110)
        for i, item in enumerate(carrito, start=1):
            subtotal = formato_pesos_clp(item["subtotal"])
            print(f"{i}. {item['nombre']} | Cant: {item['cantidad']} | Subtotal: ${subtotal}")
        print("-" * 110)

        nro = validar_entero("Ingrese el número del item a eliminar: ")
        indice = nro - 1

        eliminado = eliminar_item_por_indice(carrito, indice)

        if not eliminado:
            print("Número inválido. No se eliminó ningún item.")
            return

        print("Item eliminado y stock devuelto.")
        try:
            previsualizar_carrito(carrito)
        except NameError:
            pass


    def accion_finalizar_venta():
        if not carrito:
            print("No puedes finalizar una venta con el carrito vacío.")
            return

        total = calcular_total_recursivo(carrito)
        print(f"\nTotal venta: ${formato_pesos_clp(total)}")
        confirmacion = input("¿Confirmar venta? (s/n): ").lower().strip()

        if confirmacion != "s":
            devolver_reserva_stock(carrito)
            carrito.clear()
            print("Venta no confirmada. Stock devuelto y carrito limpiado.")
            return


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
        "3": ("Editar cantidad de un item", accion_editar_cantidad_item),
        "4": ("Eliminar item del carrito", accion_eliminar_item),
        "5": ("Finalizar venta", accion_finalizar_venta),
        "0": ("Cancelar", None)
        }


    while True:
        mostrar_menu_carrito(opciones_carrito)
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "0":
            devolver_reserva_stock(carrito)
            print("Venta cancelada. Stock devuelto.")
            return

        if opcion not in opciones_carrito:
            print("Opción inválida. Intente nuevamente.")
            continue

        accion = opciones_carrito[opcion][1]

        try:
            resultado = accion()
            if opcion == "5" and resultado is True:
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

    # 1) Devolver stock al inventario
    items = venta.get("items", [])
    for item in items:
        producto = buscar_producto_por_id(item["producto_id"])

        if not producto:
            print(f"No se encontró el producto ID {item['producto_id']} para devolver stock.")
            continue

        producto["stock"] += item["cantidad"]

    # 2) Anulación lógica
    venta["activo"] = False

    print("Venta anulada correctamente y stock devuelto al inventario.")
    mostrar_venta(venta, mostrar_detalle=False)




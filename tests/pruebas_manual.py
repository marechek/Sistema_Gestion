import builtins
import copy

from data.inventario import inventario
from data.clientes import clientes
from data.ventas import ventas

# Inventario
from servicios.inventario_service import (
    listar_productos,
    agregar_producto,
    actualizar_stock,
    activar_producto,
    desactivar_producto,
    buscar_producto_por_id
)

# Clientes
from servicios.clientes_service import (
    listar_clientes,
    registrar_cliente,
    modificar_cliente,
    activar_cliente,
    desactivar_cliente
)

# Ventas
from servicios.ventas_service import (
    crear_venta,
    listar_ventas,
    ver_detalle_venta,
    anular_venta
)

# Reportes
from servicios.reportes_service import (
    reporte_resumen_inventario,
    reporte_inventario_por_categoria,
    reporte_resumen_ventas,
    reporte_top_productos_vendidos,
    reporte_top_clientes_por_monto,
    reporte_clientes_activos_inactivos
)


# ----------------------------
# Mock input (sin librerías)
# ----------------------------

def simular_inputs(respuestas):
    """
    Reemplaza temporalmente input() para devolver respuestas predefinidas.
    """
    respuestas = list(respuestas)
    input_real = builtins.input

    def input_falso(prompt=""):
        print(prompt, end="")
        if respuestas:
            r = str(respuestas.pop(0))
            print(r)
            return r
        print("")  # Enter si faltan respuestas
        return ""

    builtins.input = input_falso
    return input_real


def restaurar_input(input_real):
    builtins.input = input_real


# ----------------------------
# Helpers de verificación
# ----------------------------

def stock_producto(producto_id):
    p = buscar_producto_por_id(producto_id)
    if not p:
        print(f"⚠ Producto {producto_id} no encontrado.")
        return None
    return p["stock"]


def mostrar_stock(producto_id, etiqueta=""):
    p = buscar_producto_por_id(producto_id)
    if not p:
        print(f"⚠ Producto {producto_id} no encontrado.")
        return None
    extra = f" ({etiqueta})" if etiqueta else ""
    print(f"Stock producto {producto_id} - {p['nombre']}{extra}: {p['stock']}")
    return p["stock"]


# ----------------------------
# Tests por módulo
# ----------------------------

def test_inventario():
    print("\n==============================")
    print("TEST MÓDULO: INVENTARIO")
    print("==============================")

    print("\n1) Listar productos")
    listar_productos()

    print("\n2) Agregar producto (simulado)")
    # agregar_producto(): Nombre, Categoría, Precio, Stock, Stock mínimo
    input_real = simular_inputs([
        "Snack Dental Perro 500g",
        "Alimentos",     # acepta nombre categoría
        "7990",          # precio
        "10",            # stock
        "3"              # stock mínimo
    ])
    try:
        agregar_producto()
    finally:
        restaurar_input(input_real)

    print("\n3) Actualizar stock del último producto agregado (simulado)")
    ultimo_id = inventario[-1]["id"]
    input_real = simular_inputs([
        str(ultimo_id),  # ID producto
        "20"             # nuevo stock
    ])
    try:
        actualizar_stock()
    finally:
        restaurar_input(input_real)

    print("\n4) Desactivar y activar producto (simulado)")
    input_real = simular_inputs([str(ultimo_id)])
    try:
        desactivar_producto()
    finally:
        restaurar_input(input_real)

    input_real = simular_inputs([str(ultimo_id)])
    try:
        activar_producto()
    finally:
        restaurar_input(input_real)

    print("\n✅ INVENTARIO OK")


def test_clientes():
    print("\n==============================")
    print("TEST MÓDULO: CLIENTES")
    print("==============================")

    print("\n1) Listar clientes")
    listar_clientes()

    print("\n2) Registrar cliente (simulado)")
    # registrar_cliente(): Nombre, RUT, Teléfono, Email, Dirección
    input_real = simular_inputs([
        "Test Cliente QA",
        "10.111.222-3",
        "911111111",
        "qa.cliente@email.com",
        "Av. QA 123, Santiago"
    ])
    try:
        registrar_cliente()
    finally:
        restaurar_input(input_real)

    print("\n3) Modificar cliente recién creado (simulado)")
    nuevo_id = clientes[-1]["id"]
    input_real = simular_inputs([
        str(nuevo_id),          # ID cliente
        "Test Cliente QA Mod",  # nombre
        "",                     # teléfono (mantener)
        "qa.mod@email.com",     # email
        ""                      # dirección (mantener)
    ])
    try:
        modificar_cliente()
    finally:
        restaurar_input(input_real)

    print("\n4) Desactivar y activar cliente (simulado)")
    input_real = simular_inputs([str(nuevo_id)])
    try:
        desactivar_cliente()
    finally:
        restaurar_input(input_real)

    input_real = simular_inputs([str(nuevo_id)])
    try:
        activar_cliente()
    finally:
        restaurar_input(input_real)

    print("\n✅ CLIENTES OK")


def test_ventas_con_reserva_unificacion_edicion_eliminacion():
    """
    Este test valida:
    - Reserva de stock al agregar
    - Cancelación devuelve reserva
    - Unificación de items repetidos
    - Editar cantidad ajusta stock
    - Eliminar item devuelve stock
    - Finalizar deja stock reservado
    - Anular venta devuelve stock
    """
    print("\n==============================")
    print("TEST MÓDULO: VENTAS (FULL UX + RESERVA)")
    print("==============================")

    # Asumimos IDs base (según tu inventario inicial):
    # Producto 1 y 3 existen y están activos.
    prod_a = 1
    prod_b = 3
    cliente_id = 1

    print("\n0) Listar ventas (estado inicial)")
    listar_ventas()

    # --- Caso 1: Reserva + Cancelar (devuelve stock) ---
    print("\n1) Reserva de stock + Cancelar (debe devolver stock)")
    stock_a_antes = mostrar_stock(prod_a, "antes reserva/cancel")

    input_real = simular_inputs([
        str(cliente_id),  # seleccionar cliente
        "1",              # agregar producto
        str(prod_a),      # id producto
        "1",              # cantidad
        "0"               # cancelar venta => devuelve reserva
    ])
    try:
        crear_venta()
    finally:
        restaurar_input(input_real)

    stock_a_despues = mostrar_stock(prod_a, "después cancel (debe ser igual)")
    if stock_a_antes is not None and stock_a_despues is not None:
        print(f"Comparación stock producto {prod_a}: antes={stock_a_antes} después={stock_a_despues}")

    # --- Caso 2: Unificación + Editar + Eliminar + Finalizar ---
    print("\n2) Unificación + Editar cantidad + Eliminar item + Finalizar")

    stock_a_inicio = mostrar_stock(prod_a, "inicio caso 2")
    stock_b_inicio = mostrar_stock(prod_b, "inicio caso 2")

    # Flujo inputs (según tu menú carrito actual):
    # 1 Agregar producto
    # 2 Ver carrito
    # 3 Editar cantidad
    # 4 Eliminar item
    # 5 Finalizar venta
    #
    # Secuencia:
    # - Agregar prod_a x1
    # - Agregar prod_a x2 (debe unificar => queda cantidad 3 en una sola línea)
    # - Ver carrito
    # - Editar item 1 -> nueva cantidad 2 (devuelve 1 unidad a stock)
    # - Agregar prod_b x1 (queda como item 2)
    # - Eliminar item 2 (devuelve stock prod_b)
    # - Finalizar venta (confirmar s)
    input_real = simular_inputs([
        str(cliente_id),  # cliente

        "1", str(prod_a), "1",   # add A x1
        "1", str(prod_a), "2",   # add A x2 (unifica)
        "2",                     # ver carrito

        "3", "1", "2",           # editar item #1 -> cantidad 2

        "1", str(prod_b), "1",   # add B x1
        "4", "2",                # eliminar item #2 (B)
        "2",                     # ver carrito

        "5", "s"                 # finalizar + confirmar
    ])
    try:
        crear_venta()
    finally:
        restaurar_input(input_real)

    print("\n3) Listar ventas (post-finalización)")
    listar_ventas()

    ultima_venta_id = ventas[-1]["id"]
    print(f"\n4) Ver detalle de la última venta (ID {ultima_venta_id})")
    input_real = simular_inputs([str(ultima_venta_id)])
    try:
        ver_detalle_venta()
    finally:
        restaurar_input(input_real)

    # Validación de stocks tras finalizar:
    # - prod_a: debería terminar con reserva equivalente a la venta final (cantidad 2)
    # - prod_b: se agregó y se eliminó antes de finalizar, debería quedar igual que al inicio
    stock_a_post_finalizar = mostrar_stock(prod_a, "post finalizar (debe bajar vs inicio)")
    stock_b_post_finalizar = mostrar_stock(prod_b, "post finalizar (debe igualar inicio)")

    # --- Caso 3: Anular última venta (devuelve stock) ---
    print("\n5) Anular última venta (debe devolver stock de la venta)")
    input_real = simular_inputs([str(ultima_venta_id), "s"])
    try:
        anular_venta()
    finally:
        restaurar_input(input_real)

    stock_a_post_anular = mostrar_stock(prod_a, "post anular (debe volver a inicio)")
    if stock_a_inicio is not None and stock_a_post_anular is not None:
        print(f"Comparación stock producto {prod_a}: inicio={stock_a_inicio} post_anular={stock_a_post_anular}")

    print("\n✅ VENTAS OK")


def test_reportes():
    print("\n==============================")
    print("TEST MÓDULO: REPORTES")
    print("==============================")

    reporte_resumen_inventario()
    reporte_inventario_por_categoria()
    reporte_clientes_activos_inactivos()
    reporte_resumen_ventas()
    reporte_top_productos_vendidos()
    reporte_top_clientes_por_monto()

    print("\n✅ REPORTES OK")


# ----------------------------
# Runner general (todo el proyecto)
# ----------------------------

def run_all():
    print("\n==============================")
    print("PRUEBAS MANUALES - TODO EL PROYECTO")
    print("==============================")

    # Snapshot para que sea repetible (idempotente)
    inv_backup = copy.deepcopy(inventario)
    cli_backup = copy.deepcopy(clientes)
    ven_backup = copy.deepcopy(ventas)

    try:
        test_inventario()
        test_clientes()
        test_ventas_con_reserva_unificacion_edicion_eliminacion()
        test_reportes()

        print("\n🎉 TODO OK: Inventario + Clientes + Ventas (FULL) + Reportes")
    finally:
        # Restaurar estado
        inventario.clear()
        inventario.extend(inv_backup)

        clientes.clear()
        clientes.extend(cli_backup)

        ventas.clear()
        ventas.extend(ven_backup)


if __name__ == "__main__":
    run_all()

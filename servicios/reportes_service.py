from data.inventario import inventario, CATEGORIAS
from data.clientes import clientes
from data.ventas import ventas

from utils.validaciones import formato_pesos_clp


def _ventas_activas():
    return [v for v in ventas if v.get("activo", True)]


def _ventas_anuladas():
    return [v for v in ventas if not v.get("activo", True)]


def _productos_activos():
    return [p for p in inventario if p.get("activo", True)]


def _productos_inactivos():
    return [p for p in inventario if not p.get("activo", True)]


def reporte_resumen_inventario():
    print("\nREPORTE: RESUMEN INVENTARIO")
    print("-" * 110)

    total = len(inventario)
    activos = len(_productos_activos())
    inactivos = len(_productos_inactivos())

    stock_bajo = 0
    sin_stock = 0

    for p in inventario:
        if p["stock"] <= p["stock_minimo"]:
            stock_bajo += 1
        if p["stock"] == 0:
            sin_stock += 1

    print(f"Total productos: {total}")
    print(f"Productos activos: {activos}")
    print(f"Productos inactivos: {inactivos}")
    print(f"Productos con stock bajo (<= mínimo): {stock_bajo}")
    print(f"Productos sin stock (= 0): {sin_stock}")
    print("-" * 110)


def reporte_inventario_por_categoria():
    print("\nREPORTE: INVENTARIO POR CATEGORÍA")
    print("-" * 110)

    conteo = {cat_id: 0 for cat_id in CATEGORIAS.keys()}

    for p in inventario:
        cat_id = p["categoria_id"]
        if cat_id in conteo:
            conteo[cat_id] += 1

    for cat_id, cantidad in conteo.items():
        print(f"{CATEGORIAS[cat_id]}: {cantidad} productos")

    print("-" * 110)


def reporte_resumen_ventas():
    print("\nREPORTE: RESUMEN VENTAS")
    print("-" * 110)

    activas = _ventas_activas()
    anuladas = _ventas_anuladas()

    total_activas = len(activas)
    total_anuladas = len(anuladas)

    monto_total = 0
    for v in activas:
        monto_total += v.get("total", 0)

    ticket_promedio = (monto_total / total_activas) if total_activas > 0 else 0

    print(f"Ventas activas: {total_activas}")
    print(f"Ventas anuladas: {total_anuladas}")
    print(f"Monto total (ventas activas): ${formato_pesos_clp(monto_total)}")
    print(f"Ticket promedio (ventas activas): ${formato_pesos_clp(ticket_promedio)}")
    print("-" * 110)


def reporte_top_productos_vendidos(top_n=5):
    print("\nREPORTE: TOP PRODUCTOS VENDIDOS (VENTAS ACTIVAS)")
    print("-" * 110)

    activas = _ventas_activas()

    acumulado = {}

    for v in activas:
        for item in v.get("items", []):
            pid = item["producto_id"]
            if pid not in acumulado:
                acumulado[pid] = {"nombre": item["nombre"], "cantidad": 0, "monto": 0}
            acumulado[pid]["cantidad"] += item["cantidad"]
            acumulado[pid]["monto"] += item["subtotal"]

    if not acumulado:
        print("No hay ventas activas para analizar.")
        print("-" * 110)
        return

    # ordenar por cantidad desc
    ranking = sorted(acumulado.items(), key=lambda x: x[1]["cantidad"], reverse=True)

    # set: productos únicos vendidos (consigna)
    productos_unicos = {pid for pid, _ in ranking}
    print(f"Productos únicos vendidos: {len(productos_unicos)}\n")

    limite = min(top_n, len(ranking))
    for i in range(limite):
        pid, data = ranking[i]
        print(
            f"{i+1}. ID {pid} | {data['nombre']} | "
            f"Unidades: {data['cantidad']} | "
            f"Monto: ${formato_pesos_clp(data['monto'])}"
        )

    print("-" * 110)


def reporte_top_clientes_por_monto(top_n=5):
    print("\nREPORTE: TOP CLIENTES POR MONTO (VENTAS ACTIVAS)")
    print("-" * 110)

    activas = _ventas_activas()

    # dict: cliente_id -> {"nombre":..., "monto":..., "ventas":...}
    acumulado = {}

    for v in activas:
        cid = v.get("cliente_id")
        nombre = v.get("cliente_nombre", "N/A")
        total = v.get("total", 0)

        if cid not in acumulado:
            acumulado[cid] = {"nombre": nombre, "monto": 0, "ventas": 0}

        acumulado[cid]["monto"] += total
        acumulado[cid]["ventas"] += 1

    if not acumulado:
        print("No hay ventas activas para analizar.")
        print("-" * 110)
        return

    ranking = sorted(acumulado.items(), key=lambda x: x[1]["monto"], reverse=True)

    limite = min(top_n, len(ranking))
    for i in range(limite):
        cid, data = ranking[i]
        print(
            f"{i+1}. ID Cliente {cid} | {data['nombre']} | "
            f"Ventas: {data['ventas']} | "
            f"Monto: ${formato_pesos_clp(data['monto'])}"
        )

    print("-" * 110)


def reporte_clientes_activos_inactivos():
    print("\nREPORTE: CLIENTES ACTIVOS / INACTIVOS")
    print("-" * 110)

    total = len(clientes)
    activos = 0
    inactivos = 0

    for c in clientes:
        if c.get("activo", True):
            activos += 1
        else:
            inactivos += 1

    print(f"Total clientes: {total}")
    print(f"Clientes activos: {activos}")
    print(f"Clientes inactivos: {inactivos}")
    print("-" * 110)

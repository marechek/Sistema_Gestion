from servicios.reportes_service import (
    reporte_resumen_inventario,
    reporte_inventario_por_categoria,
    reporte_resumen_ventas,
    reporte_top_productos_vendidos,
    reporte_top_clientes_por_monto,
    reporte_clientes_activos_inactivos
)


def mostrar_menu(opciones):
    print("\nMENÚ REPORTES")
    for key, valor in opciones.items():
        print(f"{key}. {valor[0]}")


def menu_reportes():
    opciones = {
        "1": ("Resumen inventario", reporte_resumen_inventario),
        "2": ("Inventario por categoría", reporte_inventario_por_categoria),
        "3": ("Resumen ventas", reporte_resumen_ventas),
        "4": ("Top productos vendidos", reporte_top_productos_vendidos),
        "5": ("Top clientes por monto", reporte_top_clientes_por_monto),
        "6": ("Clientes activos / inactivos", reporte_clientes_activos_inactivos),
        "0": ("Volver al menú principal", None)
    }

    while True:
        mostrar_menu(opciones)
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "0":
            print("Volviendo al menú principal...")
            break

        if opcion not in opciones:
            print("Opción inválida. Intente nuevamente.")
            continue

        accion = opciones[opcion][1]

        try:
            accion()
        except Exception as e:
            print("Ocurrió un error al ejecutar la opción.")
            print(f"Detalle técnico: {e}")

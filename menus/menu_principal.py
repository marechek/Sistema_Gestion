from menus.menu_inventario import menu_inventario
from menus.menu_clientes import menu_clientes
from menus.menu_ventas import menu_ventas
from menus.menu_reportes import menu_reportes
from menus.menu_ventas import menu_ventas

def mostrar_menu(opciones):
    print("\nMENÚ PRINCIPAL")
    for key, valor in opciones.items():
        print(f"{key}. {valor[0]}")

def menu_principal():
    opciones = {
        "1": ("Módulo Inventario", menu_inventario),
        "2": ("Módulo Clientes", menu_clientes),
        "3": ("Módulo Ventas", menu_ventas),
        "4": ("Reportes", menu_reportes),
        "0": ("Salir", None)
    }

    while True:
        mostrar_menu(opciones)
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "0":
            print("Saliendo del sistema...")
            break

        if opcion not in opciones:
            print("Opción inválida. Intente nuevamente.")
            continue

        accion = opciones[opcion][1]

        if accion is None:
            print("Módulo aún no implementado.")
            continue

        try:
            accion()
        except Exception as e:
            print("Ocurrió un error al ejecutar el módulo.")
            print(f"Detalle técnico: {e}")

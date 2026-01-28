# Menú del módulo Inventario

from servicios.inventario_service import (
    listar_productos,
    agregar_producto,
    actualizar_stock,
    desactivar_producto,
    activar_producto
)

def mostrar_menu(opciones):
    print("\nMENÚ INVENTARIO")
    for key, valor in opciones.items():
        texto = valor[0]
        print(f"{key}. {texto}")

def menu_inventario():
    opciones = {
        "1": ("Listar productos", listar_productos),
        "2": ("Agregar producto", agregar_producto),
        "3": ("Actualizar stock", actualizar_stock),
        "4": ("Activar producto", activar_producto),
        "5": ("Desactivar producto", desactivar_producto),
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

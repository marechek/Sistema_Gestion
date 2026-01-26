# Menú del módulo Inventario

from servicios.inventario_service import (
    listar_productos,
    agregar_producto,
    actualizar_stock,
    desactivar_producto,
    activar_producto
)


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
        print("\nMENÚ INVENTARIO")
        for key, valor in opciones.items():
            texto = valor[0]
            print(f"{key}. {texto}")

        opcion = input("Seleccione una opción: ")

        if opcion == "0":
            print("Volviendo al menú principal...")
            break

        accion = opciones.get(opcion)

        if accion:
            accion[1]()
        else:
            print("Opción inválida. Intente nuevamente.")

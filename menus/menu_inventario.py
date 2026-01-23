# Menú del módulo Inventario

from servicios.inventario_service import (
    listar_productos,
    agregar_producto,
    actualizar_stock,
    eliminar_producto
)


def menu_inventario():
    while True:
        print("\nMENÚ INVENTARIO")
        print("1. Listar productos")
        print("2. Agregar producto")
        print("3. Actualizar stock")
        print("4. Eliminar producto")
        print("0. Volver al menú principal")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            listar_productos()

        elif opcion == "2":
            agregar_producto()

        elif opcion == "3":
            actualizar_stock()

        elif opcion == "4":
            eliminar_producto()

        elif opcion == "0":
            print("Volviendo al menú principal...")
            break

        else:
            print("Opción inválida. Intente nuevamente.")

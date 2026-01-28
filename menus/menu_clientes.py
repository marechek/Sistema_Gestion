# Menú del módulo Clientes

from servicios.clientes_service import (
    listar_clientes,
    registrar_cliente,
    modificar_cliente,
    activar_cliente,
    desactivar_cliente
)

def mostrar_menu(opciones):
    print("\nMENÚ CLIENTES")
    for key, valor in opciones.items():
        print(f"{key}. {valor[0]}")

def menu_clientes():
    opciones = {
        "1": ("Listar clientes", listar_clientes),
        "2": ("Registrar cliente", registrar_cliente),
        "3": ("Modificar cliente", modificar_cliente),
        "4": ("Activar cliente", activar_cliente),
        "5": ("Desactivar cliente", desactivar_cliente),
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

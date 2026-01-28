from servicios.ventas_service import crear_venta


def mostrar_menu(opciones):
    print("\nMENÚ VENTAS")
    for key, valor in opciones.items():
        print(f"{key}. {valor[0]}")


def menu_ventas():
    opciones = {
        "1": ("Crear venta", crear_venta),
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

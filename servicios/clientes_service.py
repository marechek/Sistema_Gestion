# Lógica de negocio del módulo Clientes

from data.clientes import clientes
from utils.validaciones import validar_texto_no_vacio, validar_entero

def obtener_ids_existentes():
    return {cliente["id"] for cliente in clientes}

def generar_id_cliente(id_actual=1):
    ids_existentes = obtener_ids_existentes()

    if id_actual not in ids_existentes:
        return id_actual

    return generar_id_cliente(id_actual + 1)

def buscar_cliente_por_id(id_cliente):
    for cliente in clientes:
        if cliente["id"] == id_cliente:
            return cliente
    return None


def mostrar_cliente(cliente):
    estado = "Activo" if cliente["activo"] else "Inactivo"

    print(
        f"ID: {cliente['id']} | "
        f"Nombre: {cliente['nombre']} | "
        f"RUT: {cliente['rut']} | "
        f"Tel: {cliente['telefono']} | "
        f"Email: {cliente['email']} | "
        f"Dirección: {cliente['direccion']} | "
        f"Estado: {estado}"
    )

def listar_clientes():
    if not clientes:
        print("\nNo hay clientes registrados.")
        return

    print("\nLISTADO DE CLIENTES")
    print("-" * 110)

    for cliente in clientes:
        mostrar_cliente(cliente)

    print("-" * 110)

def registrar_cliente():
    print("\nREGISTRAR CLIENTE")

    id_cliente = generar_id_cliente()
    print(f"ID asignado automáticamente: {id_cliente}")

    nombre = validar_texto_no_vacio("Nombre: ")
    rut = validar_texto_no_vacio("RUT: ")
    telefono = validar_texto_no_vacio("Teléfono: ")
    email = validar_texto_no_vacio("Email: ")
    direccion = validar_texto_no_vacio("Dirección: ")

    cliente = {
        "id": id_cliente,
        "nombre": nombre,
        "rut": rut,
        "telefono": telefono,
        "email": email,
        "direccion": direccion,
        "activo": True
    }

    clientes.append(cliente)

    print("Cliente registrado correctamente.")
    mostrar_cliente(cliente)

def modificar_cliente():
    print("\nMODIFICAR CLIENTE")
    listar_clientes()

    id_cliente = validar_entero("ID del cliente a modificar: ")
    cliente = buscar_cliente_por_id(id_cliente)

    if not cliente:
        print("Cliente no encontrado.")
        return

    print("\nPresione ENTER para mantener el valor actual.\n")

    nombre = input(f"Nombre [{cliente['nombre']}]: ").strip()
    telefono = input(f"Teléfono [{cliente['telefono']}]: ").strip()
    email = input(f"Email [{cliente['email']}]: ").strip()
    direccion = input(f"Dirección [{cliente['direccion']}]: ").strip()

    if nombre:
        cliente["nombre"] = nombre
    if telefono:
        cliente["telefono"] = telefono
    if email:
        cliente["email"] = email
    if direccion:
        cliente["direccion"] = direccion

    print("Cliente actualizado correctamente.")
    mostrar_cliente(cliente)

def activar_cliente():
    print("\nACTIVAR CLIENTE")
    listar_clientes()

    id_cliente = validar_entero("ID del cliente: ")
    cliente = buscar_cliente_por_id(id_cliente)

    if not cliente:
        print("Cliente no encontrado.")
        return
    if cliente["activo"]:
        print("El cliente ya está activo.")
        return

    cliente["activo"] = True
    print("Cliente activado correctamente.")
    mostrar_cliente(cliente)

def desactivar_cliente():
    print("\nDESACTIVAR CLIENTE")
    listar_clientes()

    id_cliente = validar_entero("ID del cliente: ")
    cliente = buscar_cliente_por_id(id_cliente)

    if not cliente:
        print("Cliente no encontrado.")
        return
    if not cliente["activo"]:
        print("El cliente ya está inactivo.")
        return

    cliente["activo"] = False
    print("Cliente desactivado correctamente.")
    mostrar_cliente(cliente)


# Funciones de validación de entradas del usuario

def validar_numero(mensaje, tipo=int, minimo=0):
    """
    Solicita un número (entero o flotante) al usuario.
    Repite hasta que el valor sea válido.
    """
    while True:
        try:
            valor = tipo(input(mensaje))
            if valor < minimo:
                print(f"El valor no puede ser menor que {minimo}.")
                continue
            return valor
        except ValueError:
            tipo_nombre = "entero" if tipo == int else "numérico"
            print(f"Debes ingresar un valor {tipo_nombre} válido.")


def validar_entero(mensaje):
    return validar_numero(mensaje, int, 0)


def validar_flotante(mensaje):
    return validar_numero(mensaje, float, 0)


def validar_texto_no_vacio(mensaje):
    """
    Solicita un texto no vacío.
    """
    while True:
        texto = input(mensaje).strip()
        if not texto:
            print("El texto no puede estar vacío.")
            continue
        return texto
    

def formato_pesos_clp(valor):
    """
    Formatea un valor como pesos chilenos.
    """
    return f"{valor:,.0f}".replace(",", ".")

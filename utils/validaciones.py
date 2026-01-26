# Funciones de validación de entradas del usuario

def validar_entero(mensaje):
    """
    Solicita un número entero positivo al usuario.
    Repite hasta que el valor sea válido.
    """
    while True:
        try:
            valor = int(input(mensaje))
            if valor < 0:
                print("El valor no puede ser negativo.")
                continue
            return valor
        except ValueError:
            print("Debes ingresar un número entero válido.")


def validar_flotante(mensaje):
    """
    Solicita un número decimal positivo al usuario.
    """
    while True:
        try:
            valor = float(input(mensaje))
            if valor < 0:
                print("El valor no puede ser negativo.")
                continue
            return valor
        except ValueError:
            print("Debes ingresar un número válido.")


def validar_texto_no_vacio(mensaje):
    """
    Solicita un texto no vacío.
    """
    while True:
        texto = input(mensaje).strip()
        if texto == "":
            print("El texto no puede estar vacío.")
            continue
        return texto
    
def formato_pesos_clp(valor):
    """
    Formatea un valor como pesos chilenos.
    """
    return f"$ {valor:,.0f}".replace(",", ".")

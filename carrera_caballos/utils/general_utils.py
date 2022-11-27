import random
import utils.logging_carrera_caballos as log
def pide_datos(texto, tipo_a_devolver="int"):
    """Método que pide datos por consola al usuario y devuelve el tipo de dato indicado"""
    # Pedimos información al usuario
    valor_introducido = input(texto)
    if tipo_a_devolver == "str":
        return valor_introducido
    elif tipo_a_devolver == "int":
        if valor_introducido.isdigit():
            return int(valor_introducido)
        else:
            print("Valor incorrecto, vuelve a intentarlo")
            return pide_datos(texto, tipo_a_devolver)

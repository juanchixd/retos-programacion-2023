#########################################################################
# Author:       Juan Bautista Gonzalez
# Web:          juangonzalez.com.ar
# File:         Reto-04.py
# Title:        #56 EL GENERADOR DE CONTRASEÑAS
# Dificultad:   Media
#########################################################################
#  Enunciado:
# /*
#  * Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
#  * Podrás configurar generar contraseñas con los siguientes parámetros:
#  * - Longitud: Entre 8 y 16.
#  * - Con o sin letras mayúsculas.
#  * - Con o sin números.
#  * - Con o sin símbolos.
#  * (Pudiendo combinar todos estos parámetros entre ellos)
#  */
#########################################################################
import random
import string


def generate(length: int, upper=False, numbers=False, symbols=False):
    if length < 8 or length > 16:
        return "La longitud debe estar entre 8 y 16"

    password = ""
    chars = string.ascii_lowercase

    if upper:
        chars += string.ascii_uppercase
    if numbers:
        chars += string.digits
    if symbols:
        chars += string.punctuation

    for i in range(length):
        password += random.choice(chars)

    return password


print(generate(10))

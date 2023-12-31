#########################################################################
# Author:       Juan Bautista Gonzalez
# Web:          juangonzalez.com.ar
# File:         Reto-05.py
# Title:        #57 PRIMO, FIBONACCI Y PAR
# Dificultad:   Media
#########################################################################
# Enunciado:
# /*
#  * Escribe un programa que, dado un número, compruebe y muestre si es primo,
#  * fibonacci y par.
#  * Ejemplos:
#  * - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
#  * - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
#  */
#########################################################################

def primo_fibonacci_par(number: int):
    is_prime = True
    is_fibonacci = False
    is_even = True if number % 2 == 0 else False

    if number > 1:
        for i in range(2, number):
            if number % i == 0:
                is_prime = False
                break
    else:
        is_prime = False

    if number > 0:
        a, b = 0, 1
        while b < number:
            a, b = b, a + b
        if b == number:
            is_fibonacci = True

    print(f"{number} {'es primo' if is_prime else 'no es primo'}, "
          f"{'es fibonacci' if is_fibonacci else 'no es fibonacci'} y "
          f"{'es par' if is_even else 'es impar'}")


primo_fibonacci_par(-2)
primo_fibonacci_par(2)
primo_fibonacci_par(7)
primo_fibonacci_par(8)

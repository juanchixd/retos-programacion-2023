#########################################################################
# Author:       Juan Bautista Gonzalez
# Web:          juangonzalez.com.ar
# File:         Reto-02.py
# Title:        #54 EL "LENGUAJE HACKER"
# Dificultad:   Media
#########################################################################
# Enunciado:
# /*
#  * Escribe un programa que reciba un texto y transforme lenguaje natural a
#  * "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
#  *  se caracteriza por sustituir caracteres alfanuméricos.
#  * - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/)
#  *   con el alfabeto y los números en "leet".
#  *   (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
#  */
#########################################################################

def leetSpeak(text):
    dic_leet = {"a": "4", "b": "8", "c": "[", "d": ")", "e": "3", "f": "|=",
                "g": "&", "h": "#", "i": "1", "j": ",_|", "k": "|<", "l": "1",
                "m": "|\/|", "n": "|\|", "o": "0", "p": "|>", "q": "(_,)",
                "r": "|2", "s": "5", "t": "7", "u": "|_|", "v": "\/", "w": "\/\/",
                "x": "*", "y": "'/", "z": "2", "1": "L", "2": "R", "3": "E", "4": "A",
                "5": "S", "6": "b", "7": "T", "8": "B", "9": "g", "0": "o"}

    text_hacker = ""

    for i in text:
        if i.lower() in dic_leet.keys():
            text_hacker += dic_leet[i.lower()]
        else:
            text_hacker += i

    return text_hacker


print(leetSpeak("Hola Mundo!"))

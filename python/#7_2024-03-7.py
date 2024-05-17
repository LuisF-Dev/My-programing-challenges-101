
"""/*
* Crea un programa que invierta el orden de una cadena de texto
* sin usar funciones propias del lenguaje que lo hagan de forma automática.
* - Si le pasamos "Hola mundo" nos retornaría "odnum aloH"
*/"""

lista = []
def inverter():
    word = input("ingresa una palabra: ")
    char = len(word)
    pos= char - 1
    while char > 0:
        lista.append(word[pos:char])
        pos -= 1
        char -= 1
    inverted = "".join(lista)
    print(inverted)
inverter()

#correct.7/3/2024 //// 16/3/2024
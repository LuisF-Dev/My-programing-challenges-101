"""/*
* Crea un programa que invierta el orden de una cadena de texto
* sin usar funciones propias del lenguaje que lo hagan de forma automática.
* - Si le pasamos "Hola mundo" nos retornaría "odnum aloH"
*/"""
def reverser():
    word = input("ingresa una palabra para revertirla: ")
    reversed_letters =[]
    for letters in word:
        reversed_letters.insert(0,letters)
    reversed_word="".join(reversed_letters)
    print(reversed_word)
reverser()

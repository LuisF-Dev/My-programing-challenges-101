"""/*
 * Escribe una función que reciba dos palabras (String) y retorne
 * verdadero o falso (Bool) según sean o no anagramas.
 * - Un Anagrama consiste en formar una palabra reordenando TODAS
 *   las letras de otra palabra inicial.
 * - NO hace falta comprobar que ambas palabras existan.
 * - Dos palabras exactamente iguales no son anagrama.
 */"""
def es_un_anagrama(palabra1, palabra2):
    if len(palabra1) == len(palabra2):
        if palabra1 != palabra2 :
            palabra1=list(palabra1)
            palabra2= list(palabra2)
            if palabra1.sort() == palabra2.sort():
                return True
            else:
                return False

        else:
            return False
    else:
        return False

palabra1=input("ingresa la palabra 1: ")
palabra2 =input("ingresa la palabra 2: ")
boool = es_un_anagrama(palabra1,palabra2 )
print(boool)
#correcto
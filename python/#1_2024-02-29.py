"""
 * Escribe un programa que muestre por consola (con un print) los
 * números de 1 a 100 (ambos incluidos y con un salto de línea entre
 * cada impresión), sustituyendo los siguientes:
 * - Múltiplos de 3 por la palabra "fizz".
 * - Múltiplos de 5 por la palabra "buzz".
 * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
 *"""

numero = 0

while numero <100 :
    numero += 1
    resto = numero % 3
    resto1 = numero % 5
    if resto ==0 and resto1== 0:
        print("fizzbuzz\n")
    else:
        if resto == 0 :
            print("fizz\n")
        elif resto1 == 0 :
            print("buzz\n")
        else:
            print(f"{numero} \n")


    

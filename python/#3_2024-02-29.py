numero1 = 1
numeroanterior=0
contador= 0
while contador <50:
    print(numeroanterior, numero1, end=" ")
    numeroanterior = numero1 + numeroanterior
    numero1 +=numeroanterior
    contador += 2
    
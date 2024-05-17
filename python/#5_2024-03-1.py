"""/*
 * Crea una única función (importante que sólo sea una) que sea capaz
 * de calcular y retornar el área de un polígono.
 * - La función recibirá por parámetro sólo UN polígono a la vez.
 * - Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
 * - Imprime el cálculo del área de un polígono de cada tipo.
 */"""

def cal_area(lista): #poligono 1 triangulo el 2 cuadrado 3 rectangulo
    if pol == 1:
        result = side1 * side2
        return F"{result / 2}{unit}"  #AQUI NO USE UNA VARIABLE HEIGHT PARA SIMPLIFICAR LAS COSAS
    if pol == 2:
        return f"{side1 ** 2}{unit}"
    if pol == 3:
        return f"{side1 * side2 }{unit}"
pol = int(input("Ingresa que tipo de poligono es: \n1 Triangulo \n2 Cuadrado \n3 Rectangulo \nseleccion: "))
unit = str(input("Que unidad de medida vas a usar ?\n"))
if pol == 1:# triangulo
    side1 = int(input("Cuanto mide la base del triangulo: \n"))
    side2 = int(input("Cuanto mide la altura del triangulo: \n"))
if pol == 2:#cuadrado
    side1 = int(input("Cuanto mide los lados del cuadrado: \n"))
    side2 ="N/A"
if pol == 3:#rectangulo
    side1 = int(input("Cuanto mide el ancho del rectangulo: \n"))
    side2 = int(input("Cuanto mide el largo del rectangulo: \n"))
lista =[side1,side2,unit]
print(cal_area(lista))
    #entre 1/3/2024 y 2/3/2024



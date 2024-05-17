
















"""/*
 * Crea un programa se encargue de transformar un número
 * decimal a binario sin utilizar funciones propias del lenguaje que lo hagan directamente.
 */"""
def division(n):
    while n > 0:
        if not n // 2 == 1 or n// 2 == 0: 
            binary.append(str(n % 2))
            n = n // 2
        else:
            binary.append(str(n % 2))
            binary.append(str(n // 2))
            binary.reverse()
            binary2 = "".join(binary)
            print(f"el numero {num_o} en binario es: {binary2}") 
            break   
num = int(input("ingresa el numero decimal para convertirlo a binario: "))
num_o = num
binary =[]
division(num)
#ready, 7/3/2024 / 8/3/2024



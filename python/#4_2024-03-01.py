"""/*
 * Escribe un programa que se encargue de comprobar si un número es o no primo.
 * Hecho esto, imprime los números primos entre 1 y 100.
 */"""

for N in range(2,101):
	if N % 2 ==0 and not N == 2 :
		p=1	
	elif N % 3 ==0 and not N == 3:
		p=1
	elif N % 5 ==0 and not N == 5: # dividir por los primeros 4 numeros primos para ver si da exacta la division
		p=1                        #es decir que si el modulo da 0 y al mismo tiempo el numero no es igual entonces si es
	elif N % 7 ==0 and not N == 7: #un numero primo
		p=1                        #////////////////////// cabe recalcar que el "p=1" es simplemente para que el if
	else:                          #no me de error, se podria decir que es un relleno
		print(N)

#1/3/2024 / 5/3/2024 ##### correcto ##### 
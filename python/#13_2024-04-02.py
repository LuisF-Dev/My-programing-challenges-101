"""/*
 * Escribe una función que reciba un texto y retorne verdadero o
 * falso (Boolean) según sean o no palíndromos.
 * Un Palíndromo es una palabra o expresión que es igual si se lee
  * de izquierda a derecha que de derecha a izquierda.
 * NO se tienen en cuenta los espacios, signos de puntuación y tildes.
 * Ejemplo: Ana lleva al oso la avellana.
 */"""

tildes={"á":"a","é":"e","í":"i","ó":"o","ú":"u","?":"","!":"",",":"",".":""," ":""}

def main(str1):
    
    str_lower = str1.lower()
    
    for key,value in tildes.items():
        str_lower= str_lower.replace(key, value)
    str_lower = list(str_lower)
    list_str = str_lower.copy()
    list_str.reverse()
    
    if list_str == str_lower:
        return True
    else:
        return False
    
    
print(main( "Ana lleva al oso la avellana."))
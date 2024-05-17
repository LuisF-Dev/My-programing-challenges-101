"""/*
 * Crea una función que reciba dos cadenas como parámetro (str1, str2)
 * e imprima otras dos cadenas como salida (out1, out2).
 * - out1 contendrá todos los caracteres presentes en la str1 pero NO
 *   estén presentes en str2.
 * - out2 contendrá todos los caracteres presentes en la str2 pero NO
 *   estén presentes en str1.
 */"""

def main(str1,str2):
    set_str1 = set(str1)
    set_str2 = set(str2)
    out1 = set_str1.difference(set_str2)
    out2 = set_str2.difference(set_str1)
    return "".join(out1),"".join(out2)

print(main("hola","olay"))

"2/4/2024, xd "


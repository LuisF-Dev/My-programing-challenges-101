/*
 * Escribe una función que calcule y retorne el factorial de un número dado
 * de forma recursiva.
 */
function factorial(n, n2) {
    if (n2 != undefined) {
        n = n * (n2 - 1);
        n2 = n2 - 1;
    }
    else if (n2 == undefined) {
        n2 = n;
    }
    if (n2 == 1) {
        return n;
    }
    return factorial(n, n2);
}
console.log(factorial(10));
//terminado 2024/11/02

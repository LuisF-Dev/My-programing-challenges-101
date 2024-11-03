/*
 * Escribe un programa que muestre por consola (con un print) los
 * números de 1 a 100 (ambos incluidos y con un salto de línea entre
 * cada impresión), sustituyendo los siguientes:
 * - Múltiplos de 3 por la palabra "fizz".
 * - Múltiplos de 5 por la palabra "buzz".
 * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
 */

function main() {
    for (let number = 0; number < 101; ++number) {
        if (number % 3 == 0 && number % 5 == 0) {
            console.log("fizzbuzz");
        } else if (number % 5 == 0) {
            console.log("buzz");
        } else if (number % 3 == 0) {
            console.log("fizz");
        } else {
            console.log(number);
        }
    }
}

main();

// terminado el 2024-05-17

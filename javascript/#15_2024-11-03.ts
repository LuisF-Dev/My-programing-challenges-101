/*
 * Escribe una función que calcule si un número dado es un número de Armstrong
 * (o también llamado narcisista).
 * Si no conoces qué es un número de Armstrong, debes buscar información
 * al respecto.
 */

function isArmstrong(num: number | string) {
    const initialNum = num;
    let finalNum: number = 0;
    num = num.toString();
    const len: number = num.length;
    let splitted: number[] | string[] = num.split("");
    splitted = splitted.map((num) => (+num) ** len); // operador unario para convertir a number
    splitted.map((num) => (finalNum += num));

    return finalNum == initialNum;
}
console.log(isArmstrong(370));

//terminado 2024/11/03

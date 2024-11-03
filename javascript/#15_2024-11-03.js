/*
 * Escribe una función que calcule si un número dado es un número de Armstrong
 * (o también llamado narcisista).
 * Si no conoces qué es un número de Armstrong, debes buscar información
 * al respecto.
 */
function isArmstrong(num) {
    var initialNum = num;
    var finalNum = 0;
    num = num.toString();
    var len = num.length;
    var splitted = num.split("");
    splitted = splitted.map(function (num) { return Math.pow((+num), len); }); // operador unario para convertir a number
    splitted.map(function (num) { return (finalNum += num); });
    return finalNum == initialNum;
}
console.log(isArmstrong(370));
//terminado 2024/11/03

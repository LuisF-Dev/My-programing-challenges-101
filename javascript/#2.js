/*
 * Escribe una función que reciba dos palabras (String) y retorne
 * verdadero o falso (Bool) según sean o no anagramas.
 * - Un Anagrama consiste en formar una palabra reordenando TODAS
 *   las letras de otra palabra inicial.
 * - NO hace falta comprobar que ambas palabras existan.
 * - Dos palabras exactamente iguales no son anagrama.
 */

function bucle_for(word){
    let list = new Array()
    for (i in word){
        list.push(word[i])
    }
    let list_sorted = list.sort()

    return JSON.stringify(list_sorted)
}

function main(word1 , word2){
    if (typeof word1 != "string" && typeof word1 != "string"){
        return false
    
    } else if (word1 == word2){
        return false;
    }
    //* palabras ordenadas en strings
    let word1_sorted_string = bucle_for(word1)
    let word2_sorted_string = bucle_for(word2)

    return word1_sorted_string == word2_sorted_string
}   

console.log(main("lao","lao"))

// terminado el 2024/05/17

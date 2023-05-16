const gerarNumeros = require('./numeros')
let numerosAleatorios = gerarNumeros(1, 10);
// console.log(numerosAleatorios);

exercicio15("Texto")

function exercicio1(texto) {
    console.log(texto)
}

function exercicio2(a, b) {
    console.log(`A soma é: ${a + b}`)

}

function exercicio3(vetor) {
    vetor.forEach(e => {
        console.log(e)
    });
}

function exercicio4(argumento) {
    console.log(typeof(argumento))
}

function exercicio5(numero) {
    if (numero %2 == 0) {
        console.log("Par")
    } else {
        console.log("Ímpar")
    }
}

function exercicio6(numeros) {
    let maior = numeros[0]
    numeros.forEach(e => {
        maior = e > maior ? maior = e : maior = maior
    })
    console.log(maior)
}

function exercicio7(numeros) {
    let menor = numeros[0]
    numeros.forEach(e => {
        menor = e < menor ? menor = e : menor = menor
    })
    console.log(menor)
}

function exercicio8(texto) {
    return texto.length
}

function exercicio9(textos) {
    textos.forEach(e => {
        console.log(e)
    })
}

function exercicio10(vetor) {
    let meio = Math.floor(vetor.length / 2)
    return vetor[meio]
}

function exercicio11() {
    for(let i = 1; i <= 10; i++) {
        console.log(i)
    }
}

function exercicio12(vetor) {
    let soma = vetor.reduce((soma, i) => soma + i)
    return soma 
}

function exercicio13(vetor) {
    let soma = vetor.reduce((soma, i) => soma + i)
    let media = soma / vetor.length
    return media
}

function exercicio14(numero) {
    var vetor = []
    for (let i = 1; i <= numero; i++) {
        vetor.push(i)
    }
    console.log(vetor)
    return vetor
}

function exercicio15(texto) {

    console.log(texto.split("").reverse().join(""))
}

function exercicio16() {

}

function exercicio17() {

}

function exercicio18() {

}

function exercicio19() {

}

function exercicio20() {

}

function exercicio21() {

}

function exercicio22() {

}

function exercicio23() {

}

function exercicio24() {

}

function exercicio25() {

}

function exercicio26() {

}

function exercicio27() {

}

function exercicio28() {

}

function exercicio29() {

}

function exercicio30() {

}

function exercicio31() {

}

function exercicio32() {

}

function exercicio33() {

}

function exercicio34() {

}

function exercicio35() {

}

function exercicio36() {

}

function exercicio37() {

}

function exercicio38() {

}

function exercicio39() {

}

function exercicio40() {

}

function exercicio41() {

}

function exercicio42() {

}

function exercicio43() {

}

function exercicio44() {

}

function exercicio45() {

}

function exercicio46() {

}

function exercicio47() {

}

function exercicio48() {

}

function exercicio49() {

}

function exercicio50() {

}

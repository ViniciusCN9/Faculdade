// Instale o modulo: npm install prompt-sync
const prompt = require('prompt-sync')({ sigint: true })

console.log("\nEXERCÍCIO 01:")
exercise01()
console.log("\nEXERCÍCIO 02:")
exercise02()
console.log("\nEXERCÍCIO 03:")
exercise03()
console.log("\nEXERCÍCIO 04:")
exercise04()
console.log("\nEXERCÍCIO 05:")
exercise05()

function exercise01() {
    let firstNumber = Number(prompt("Digite o 1° número: "))
    let secondNumber = Number(prompt("Digite o 2° número: "))

    if (firstNumber === secondNumber) {
        console.log(`Os números são iguais: ${firstNumber} e ${secondNumber}`)
    } else {
        console.log(`O maior valor é: ${Math.max(firstNumber, secondNumber)}`)
    }
}

function exercise02() {
    let firstNote = Number(prompt("Digite a 1° nota: ")) * 4
    let secondNote = Number(prompt("Digite a 2° nota: ")) * 3
    let thirdNote = Number(prompt("Digite a 3° nota: ")) * 3

    let average = (firstNote + secondNote + thirdNote) / (4 + 3 + 3)
    if (average >= 7) {
        console.log(`Aprovado com média: ${average}`)
    } else if (average >= 5) {
        console.log(`Recuperação com média: ${average}`)
    } else {
        console.log(`Reprovado com média: ${average}`)
    }
}

function exercise03() {
    let number = Number(prompt("Digite o número: "))
    if (number % 2) {
        console.log(`O número ${number} é par`)
    } else {
        console.log(`O número ${number} é ímpar`)
    }
}

function exercise04() {
    let year = Number(prompt("Digite o ano: "))
    if (year % 4 === 0 && year % 100 !== 0 || year % 400 === 0) {
        console.log(`O ano ${year} é bissexto`)
    } else {
        console.log(`O ano ${year} não é bissexto`)
    }
}

function exercise05() {
    let firstNumber = Number(prompt("Digite o 1° número: "))
    let secondNumber = Number(prompt("Digite o 2° número: "))
    if (firstNumber % secondNumber == 0) {
        console.log(`Os valor ${firstNumber} é múltiplo de ${secondNumber}`)
    } else {
        console.log(`Os valor ${firstNumber} não é múltiplo de ${secondNumber}`)
    }
}
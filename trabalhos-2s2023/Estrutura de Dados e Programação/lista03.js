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
    let number = Number(prompt("Digite o número: "))
    let result = []
    for (number; number >= 0; number--) {
        result.push(number)
    }
    console.log(result)
}

function exercise02() {
    let number = Number(prompt("Digite o número: "))
    let result = 0
    for (number; number >= 0; number--) {
        result += number
    }
    console.log(`A soma dos antecessóres é: ${result}`)
}

function exercise03() {
    let number = Number(prompt("Digite o número: "))
    let result = []
    for (let i = 0; i <= 10; i++) {
        result.push(`${number} X ${i} = ${number * i}`)
    }
    console.log(result)
}

function exercise04() {
    let number = Number(prompt("Digite o número: "))
    let result = 0
    for (let i = 0; i <= number; i++) {
        result += i ** 2
    }
    console.log(`A soma do quadrado dos ${number}° primeiros numeros inteiros positivos é: ${result}`)
}

function exercise05() {
    let multiples = []
    for (let i = 1; i <= 100; i++) {
        if (i % 3 == 0) {
            multiples.push(i)
        }
    }
    console.log(`Os múltiplos de 3 de 1 a 100 são: ${multiples}`)
}
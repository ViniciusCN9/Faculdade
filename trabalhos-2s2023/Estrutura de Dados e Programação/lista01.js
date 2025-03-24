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
    let thirdNumber = Number(prompt("Digite o 3° número: "))
    let result = firstNumber + (secondNumber * thirdNumber)
    console.log(`A soma do primeiro pelo segundo multiplicado pelo terceiro é: ${result}`)
}

function exercise02() {
    let firstNumber = Number(prompt("Digite o 1° número: "))
    let secondNumber = Number(prompt("Digite o 2° número: "))
    let plus = firstNumber + secondNumber
    let minus = firstNumber - secondNumber
    let multiplication = firstNumber * secondNumber
    let division = firstNumber / secondNumber
    console.log(`A soma do primeiro pelo segundo é: ${plus}`)
    console.log(`A subtração do primeiro pelo segundo é: ${minus}`)
    console.log(`A multiplicação do primeiro pelo segundo é: ${multiplication}`)
    console.log(`A divisão do primeiro pelo segundo é: ${division}`)
}

function exercise03() {
    let firstNumber = Number(prompt("Digite o 1° número: "))
    let result = firstNumber ** 2
    console.log(`O quadrado de ${firstNumber} é: ${result}`)
}

function exercise04() {
    let actualBalance = 500.0
    let checkValue = Number(prompt("Digite o valor do cheque: "))
    let result = actualBalance + checkValue
    console.log(`Saldo atual: R$${result}`)
}

function exercise05() {
    let numberInstallments = Number(prompt("Digite o número total de prestações: "))
    let paidInstallments = Number(prompt("Digite o número de prestações pagas: "))
    let installmentValue = Number(prompt("Digite o valor das prestações: "))

    let totalPaid = installmentValue * paidInstallments
    let remainingInstallments = numberInstallments - paidInstallments
    let outstandingBalance = remainingInstallments * installmentValue
    let consortiumValue = numberInstallments * installmentValue

    console.log(`Já foram pagos: R$${totalPaid} de R$${consortiumValue}, faltando ainda: R$${outstandingBalance}`)
}




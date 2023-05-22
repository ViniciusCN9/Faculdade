const gerarNumeros = require('./numeros')
let numerosAleatorios = gerarNumeros(1, 10);
console.log(numerosAleatorios);

console.log("\033[0;32m\nExercício1:\033[0;0m")
function exercicio1(texto) {
    console.log(texto)
}
exercicio1("Olá Mundo!")

console.log("\033[0;32m\nExercício2:\033[0;0m")
function exercicio2(a, b) {
    console.log(`A soma é: ${a + b}`)

}
exercicio2(5, 3)

console.log("\033[0;32m\nExercício3:\033[0;0m")
function exercicio3(vetor) {
    vetor.forEach(e => {
        console.log(e)
    });
}
exercicio3(["a", "b", "c"])

console.log("\033[0;32m\nExercício4:\033[0;0m")
function exercicio4(argumento) {
    console.log(typeof (argumento))
}
exercicio4(5)

console.log("\033[0;32m\nExercício5:\033[0;0m")
function exercicio5(numero) {
    if (numero % 2 == 0) {
        console.log("Par")
    } else {
        console.log("Ímpar")
    }
}
exercicio5(6)

console.log("\033[0;32m\nExercício6:\033[0;0m")
function exercicio6(numeros) {
    let maior = numeros[0]
    numeros.forEach(e => {
        maior = e > maior ? maior = e : maior = maior
    })
    console.log(maior)
}
exercicio6([1, 5, 6, 2])

console.log("\033[0;32m\nExercício7:\033[0;0m")
function exercicio7(numeros) {
    let menor = numeros[0]
    numeros.forEach(e => {
        menor = e < menor ? menor = e : menor = menor
    })
    console.log(menor)
}
exercicio7([1, 5, 6, 2])

console.log("\033[0;32m\nExercício8:\033[0;0m")
function exercicio8(texto) {
    console.log(texto.length)
}
exercicio8("Texto")

console.log("\033[0;32m\nExercício9:\033[0;0m")
function exercicio9(textos) {
    textos.forEach(e => {
        console.log(e)
    })
}
exercicio9(["Era", "Vez", "Uma"])

console.log("\033[0;32m\nExercício10\033[0;0m:")
function exercicio10(vetor) {
    let meio = Math.floor(vetor.length / 2)
    console.log(vetor[meio])
}
exercicio10([10, 10, 1, 10, 10])

console.log("\033[0;32m\nExercício11\033[0;0m:")
function exercicio11() {
    for (let i = 1; i <= 10; i++) {
        console.log(i)
    }
}
exercicio11()

console.log("\033[0;32m\nExercício12\033[0;0m:")
function exercicio12(vetor) {
    let soma = vetor.reduce((soma, i) => soma + i)
    console.log(soma)
}
exercicio12([5, 6, 7])

console.log("\033[0;32m\nExercício13\033[0;0m:")
function exercicio13(vetor) {
    let soma = vetor.reduce((soma, i) => soma + i)
    let media = soma / vetor.length
    console.log(media)
}
exercicio13([5, 7, 5])

console.log("\033[0;32m\nExercício14\033[0;0m:")
function exercicio14(numero) {
    var vetor = []
    for (let i = 1; i <= numero; i++) {
        vetor.push(i)
    }
    console.log(vetor)
}
exercicio14(5)

console.log("\033[0;32m\nExercício15\033[0;0m:")
function exercicio15(texto) {
    console.log(texto.split("").reverse().join(""))
}
exercicio15("Cavalo")

console.log("\033[0;32m\nExercício16\033[0;0m:")
function exercicio16(texto) {
    let invertida = texto.split("").reverse().join("")
    console.log(texto === invertida ? true : false)
}
exercicio16("Ovo")

console.log("\033[0;32m\nExercício17\033[0;0m:")
function exercicio17(textoA, textoB) {
    if (textoA.length != textoB.length) {
        console.log(false)
        return
    }
    console.log(textoA.split("").sort().join("") == textoB.split("").sort().join(""))
}
exercicio17("orava", "avaro")

console.log("\033[0;32m\nExercício18\033[0;0m:")
function exercicio18(vetor) {
    let ordenado = vetor.sort((anterior, proximo) => {
        if (proximo.length > anterior.length) {
            return -1
        }
        if (proximo.length < anterior.length) {
            return 1
        }
        return 0
    })
    console.log(ordenado)
}
exercicio18(["Maria", "Ana", "Aparecido", "João"])

console.log("\033[0;32m\nExercício19\033[0;0m:")
function exercicio19(vetor) {
    let ordenado = vetor.sort((anterior, proximo) => {
        if (proximo > anterior) {
            return -1
        }
        if (proximo < anterior) {
            return 1
        }
        return 0
    })
    console.log(ordenado)
}
exercicio19([1, 5, 15, 2])

console.log("\033[0;32m\nExercício20\033[0;0m:")
function exercicio20(vetor) {
    let ordenado = vetor.sort((anterior, proximo) => {
        if (proximo < anterior) {
            return -1
        }
        if (proximo > anterior) {
            return 1
        }
        return 0
    })
    console.log(ordenado)
}
exercicio20([1, 5, 15, 2])

class Exercicio21 {
    constructor(dificuldade) {
        this.numero = 21
        this.dificuldade = dificuldade
    }

    exibir() {
        console.log(`O exercício é: ${this.numero} e sua dificuldade: ${this.dificuldade}`)
    }
}
var objeto = new Exercicio21("Fácil")
objeto.exibir()

console.log("\033[0;32m\nExercício22\033[0;0m:")
function exercicio22(vetor, numero) {
    vetor.includes(numero) ? console.log("Existe") : console.log("Existe")
}
exercicio22([1, 5, 10], 5)

console.log("\033[0;32m\nExercício23\033[0;0m:")
function exercicio23() {
    exercicio6([1, 5, 6, 2])
}
exercicio23()

console.log("\033[0;32m\nExercício24\033[0;0m:")
function exercicio24() {
    exercicio7([1, 5, 6, 2])
}
exercicio24()

console.log("\033[0;32m\nExercício25\033[0;0m:")
function exercicio25(vetor, valor) {
    let contador = 0;

    for (let i = 0; i < vetor.length; i++) {
        if (vetor[i] === valor) {
            contador++
        }
    }

    console.log(contador)
}
exercicio25([1, 5, 10], 5)

console.log("\033[0;32m\nExercício26\033[0;0m:")
function exercicio26(vetor) {
    let novoVetor = []

    for (let i = 0; i < vetor.length; i++) {
        if (!novoVetor.includes(vetor[i])) {
            novoVetor.push(vetor[i])
        }
    }

    console.log(novoVetor)
}
exercicio26([5, 2, 2, 9])

console.log("\033[0;32m\nExercício27\033[0;0m:")
function exercicio27(texto) {
    const caracteres = {}
    let novoTexto = ""

    for (let i = 0; i < texto.length; i++) {
        if (!caracteres[texto[i]]) {
            caracteres[texto[i]] = true
            novoTexto += texto[i]
        }
    }

    console.log(novoTexto)
}
exercicio27("Vaazio")

console.log("\033[0;32m\nExercício28\033[0;0m:")
function exercicio28(vetor) {
    let novoVetor = [];

    for (let i = 0; i < vetor.length; i++) {
        novoVetor.push(vetor[i] * 2);
    }

    console.log(novoVetor);
}
exercicio28([1, 3, 5])

console.log("\033[0;32m\nExercício29\033[0;0m:")
function exercicio29(vetor) {
    let comprimentos = []

    for (let i = 0; i < vetor.length; i++) {
        comprimentos.push(vetor[i].length)
    }

    console.log(comprimentos)
}
exercicio29(["Um", "Dois"])

console.log("\033[0;32m\nExercício30\033[0;0m:")
function exercicio30(texto) {
    console.log(texto.toUpperCase())
}
exercicio30("teste")

console.log("\033[0;32m\nExercício31\033[0;0m:")
function exercicio31(texto) {
    console.log(texto.toLowerCase())
}
exercicio31("TESTE")

console.log("\033[0;32m\nExercício32\033[0;0m:")
function exercicio32(vetor) {
    let soma = 0

    for (let i = 0; i < vetor.length; i++) {
        if (vetor[i] % 2 === 0) {
            soma += vetor[i]
        }
    }

    console.log(soma)
}
exercicio32([1, 2, 3, 4, 5, 6])

console.log("\033[0;32m\nExercício33\033[0;0m:")
function exercicio33(vetor) {
    let soma = 0

    for (let i = 0; i < vetor.length; i++) {
        if (vetor[i] % 2 !== 0) {
            soma += vetor[i]
        }
    }

    console.log(soma)
}
exercicio33([1, 2, 3, 4, 5, 6])

console.log("\033[0;32m\nExercício34\033[0;0m:")
function exercicio34(vetor) {
    let vetorPares = []

    for (let i = 0; i < vetor.length; i++) {
        if (vetor[i] % 2 === 0) {
            vetorPares.push(vetor[i])
        }
    }

    console.log(vetorPares)
}
exercicio34([1, 2, 3, 4, 5, 6])

console.log("\033[0;32m\nExercício35\033[0;0m:")
function exercicio35(vetor) {
    let vetorImpares = []

    for (let i = 0; i < vetor.length; i++) {
        if (vetor[i] % 2 !== 0) {
            vetorImpares.push(vetor[i])
        }
    }

    console.log(vetorImpares)
}
exercicio35([1, 2, 3, 4, 5, 6])

console.log("\033[0;32m\nExercício36\033[0;0m:")
function exercicio36(texto) {
    let vogais = ['a', 'e', 'i', 'o', 'u']
    let contador = 0

    for (let i = 0; i < texto.length; i++) {
        let char = texto[i].toLowerCase()
        if (vogais.includes(char)) {
            contador++
        }
    }

    console.log(contador)
}
exercicio36("Testando")

console.log("\033[0;32m\nExercício37\033[0;0m:")
function exercicio37(texto) {
    let vogais = ['a', 'e', 'i', 'o', 'u']
    let contador = 0

    for (let i = 0; i < texto.length; i++) {
        let char = texto[i].toLowerCase()
        if (!vogais.includes(char)) {
            contador++
        }
    }

    console.log(contador)
}
exercicio37("Testando")

console.log("\033[0;32m\nExercício38\033[0;0m:")
function exercicio38(texto, caractere) {
    let contador = 0

    for (let i = 0; i < texto.length; i++) {
        if (texto[i].toLowerCase() === caractere.toLowerCase()) {
            contador++
        }
    }

    console.log(contador)
}
exercicio38("Testando", "t")

console.log("\033[0;32m\nExercício39\033[0;0m:")
function exercicio39(numero) {
    for (let i = 1; i <= 10; i++) {
        let resultado = numero * i
        console.log(numero + ' x ' + i + ' = ' + resultado)
    }
}
exercicio39(5)

console.log("\033[0;32m\nExercício40\033[0;0m:")
function exercicio40(vetor) {
    let produto = 1

    for (let i = 0; i < vetor.length; i++) {
        produto *= vetor[i]
    }

    console.log(produto)
}
exercicio40([1, 2, 3, 4, 5])

console.log("\033[0;32m\nExercício41\033[0;0m:")
function exercicio41(vetor) {
    console.log(vetor.join(''))
}
exercicio41(["Teste ", "de", " concatenação"])

console.log("\033[0;32m\nExercício42\033[0;0m:")
function exercicio42(textoA, textoB) {
    textoA.includes(textoB) ? console.log("Contém") : console.log("Não contém")
}
exercicio42("Padaria", "daria")

console.log("\033[0;32m\nExercício43\033[0;0m:")
function exercicio43(texto, n) {
    console.log(texto.repeat(n))
}
exercicio43("Teste", 2)

console.log("\033[0;32m\nExercício44\033[0;0m:")
function exercicio44(vetor) {
    for (let i = 0; i < vetor.length - 1; i++) {
        if (vetor[i] > vetor[i + 1]) {
            console.log("Não está")
            return
        }
    }
    console.log("Está")
}
exercicio44([1, 2, 3, 4, 5])

console.log("\033[0;32m\nExercício45\033[0;0m:")
function exercicio45(vetor) {
    for (let i = 0; i < vetor.length - 1; i++) {
        if (vetor[i] > vetor[i + 1]) {
            console.log("Está")
            return
        }
    }
    console.log("Não está")
}
exercicio45([1, 2, 3, 4, 5])

console.log("\033[0;32m\nExercício46\033[0;0m:")
function exercicio46(texto) {
    let palavras = texto.split(' ');
    let palavrasCapitalizadas = palavras.map((palavra) => {
        return palavra.charAt(0).toUpperCase() + palavra.slice(1);
    });
    console.log(palavrasCapitalizadas.join(' '))
}
exercicio46("olá mundo")

console.log("\033[0;32m\nExercício47\033[0;0m:")
function exercicio47(numero) {
    if (numero <= 1) {
        console.log("Não é primo!")
        return false
    }

    for (let i = 2; i <= Math.sqrt(numero); i++) {
        if (numero % i === 0) {
            console.log("Não é primo!")
            return false
        }
    }

    console.log("É primo!")
    return true
}
exercicio47(13)

console.log("\033[0;32m\nExercício48\033[0;0m:")
function exercicio48(n) {
    let contador = 0
    let numero = 2

    while (contador < n) {
        if (exercicio47(numero)) {
            console.log(numero)
            contador++
        }
        numero++
    }
}
exercicio48(5)

console.log("\033[0;32m\nExercício49\033[0;0m:")
function exercicio49(vetor) {
    let numerosPrimos = []

    for (let i = 0; i < vetor.length; i++) {
        let numero = vetor[i]

        if (exercicio47(numero)) {
            numerosPrimos.push(numero)
        }
    }

    console.log(numerosPrimos)
}
exercicio49([2, 5, 13, 19, 24])

console.log("\033[0;32m\nExercício50\033[0;0m:")
function exercicio50(vetor, n) {
    let numerosMaiores = []

    for (let i = 0; i < vetor.length; i++) {
        let numero = vetor[i]

        if (numero > n) {
            numerosMaiores.push(numero)
        }
    }

    console.log(numerosMaiores)
}
exercicio50([2, 5, 8, 10, 15], 7)

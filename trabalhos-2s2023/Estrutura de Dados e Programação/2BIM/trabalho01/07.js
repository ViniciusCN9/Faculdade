const prompt = require('prompt-sync')()

function separarParesEImpares(vetor) {
    if (vetor.length !== 10) {
        console.log("O vetor deve ter exatamente 10 elementos.");
        return;
    }

    const pares = [];
    const impares = [];

    for (let i = 0; i < vetor.length; i++) {
        if (vetor[i] % 2 === 0) {
            pares.push(vetor[i]);
        } else {
            impares.push(vetor[i]);
        }
    }

    console.log("Elementos Pares:", pares);
    console.log("Elementos Ímpares:", impares);
}

// Função para ler um vetor de 10 elementos inteiros
function lerVetor() {
    const vetor = [];

    for (let i = 0; i < 10; i++) {
        const elemento = parseInt(prompt(`Informe o elemento ${i + 1}:`));

        if (isNaN(elemento)) {
            console.log("Por favor, informe um valor inteiro.");
            return;
        }

        vetor.push(elemento);
    }

    return vetor;
}

// Exemplo de uso
const meuVetor = lerVetor();

if (meuVetor) {
    separarParesEImpares(meuVetor);
}

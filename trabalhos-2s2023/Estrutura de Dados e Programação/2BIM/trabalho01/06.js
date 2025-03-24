const prompt = require('prompt-sync')()

function calcularMediaAritmetica(vetor) {
    if (vetor.length !== 10) {
        console.log("O vetor deve ter exatamente 10 elementos.");
        return;
    }

    let soma = 0;

    for (let i = 0; i < vetor.length; i++) {
        soma += vetor[i];
    }

    const media = soma / vetor.length;

    return media;
}

// Função para ler um vetor de 10 elementos reais
function lerVetor() {
    const vetor = [];

    for (let i = 0; i < 10; i++) {
        const elemento = parseFloat(prompt(`Informe o elemento ${i + 1}:`));

        if (isNaN(elemento)) {
            console.log("Por favor, informe um valor numérico.");
            return;
        }

        vetor.push(elemento);
    }

    return vetor;
}

// Exemplo de uso
const meuVetor = lerVetor();

if (meuVetor) {
    const mediaAritmetica = calcularMediaAritmetica(meuVetor);
    console.log("Vetor:", meuVetor);
    console.log("Média Aritmética:", mediaAritmetica.toFixed(2));
}

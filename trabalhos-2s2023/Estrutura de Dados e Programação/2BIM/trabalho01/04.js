function multiplicarPorIndice(vetor) {
    // Verifica se o vetor tem exatamente 20 elementos
    if (vetor.length !== 20) {
        console.log("O vetor deve ter exatamente 20 elementos.");
        return;
    }

    // Multiplica cada elemento pelo seu índice
    for (let i = 0; i < vetor.length; i++) {
        vetor[i] = vetor[i] * i;
    }

    return vetor;
}

// Função para ler um vetor de 20 números inteiros
function lerVetor() {
    const vetor = [];

    for (let i = 0; i < 20; i++) {
        // Supondo que você esteja lendo os valores de algum lugar, como um usuário
        // Neste exemplo, estou usando números aleatórios de 1 a 10
        vetor.push(Math.floor(Math.random() * 10) + 1);
    }

    return vetor;
}

// Exemplo de uso
const meuVetor = lerVetor();
console.log("Vetor original:", meuVetor);

const resultadoMultiplicacao = multiplicarPorIndice(meuVetor);
console.log("Resultado da multiplicação pelos índices:", resultadoMultiplicacao);

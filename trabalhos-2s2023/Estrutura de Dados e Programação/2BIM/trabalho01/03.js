function inverterOrdemDoVetor(vetor) {
    // Verifica se o vetor tem exatamente 20 elementos
    if (vetor.length !== 20) {
        console.log("O vetor deve ter exatamente 20 elementos.");
        return;
    }

    // Inverte a ordem dos elementos no próprio vetor
    for (let i = 0; i < Math.floor(vetor.length / 2); i++) {
        const temp = vetor[i];
        vetor[i] = vetor[vetor.length - 1 - i];
        vetor[vetor.length - 1 - i] = temp;
    }
}

// Exemplo de uso
const meuVetor = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20];

console.log("Vetor original:", meuVetor);
inverterOrdemDoVetor(meuVetor);
console.log("Vetor invertido:", meuVetor);

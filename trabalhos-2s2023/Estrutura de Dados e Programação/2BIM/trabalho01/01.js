function calcularSomaDoVetor(vetor) {
    if (vetor.length !== 15) {
        console.log("O vetor deve ter exatamente 15 elementos.");
        return;
    }

    let soma = 0;
    for (let i = 0; i < vetor.length; i++) {
        soma += vetor[i];
    }

    console.log("A soma dos elementos do vetor é: " + soma);
}

// Exemplo de uso
const meuVetor = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15];
calcularSomaDoVetor(meuVetor);

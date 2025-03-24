function somarDoisVetores(vetor1, vetor2) {
    // Verifica se os vetores têm o mesmo tamanho
    if (vetor1.length !== vetor2.length) {
        console.log("Os vetores devem ter o mesmo tamanho.");
        return;
    }

    // Inicializa o vetor resultado com zeros
    let resultado = new Array(vetor1.length).fill(0);

    // Realiza a soma dos elementos
    for (let i = 0; i < vetor1.length; i++) {
        resultado[i] = vetor1[i] + vetor2[i];
    }

    return resultado;
}

// Exemplo de uso
const vetorA = [1, 2, 3, 4, 5];
const vetorB = [6, 7, 8, 9, 10];

const vetorResultado = somarDoisVetores(vetorA, vetorB);

console.log("Vetor A:", vetorA);
console.log("Vetor B:", vetorB);
console.log("Resultado da soma:", vetorResultado);

const prompt = require('prompt-sync')()

function realizarOperacoes(vetor1, vetor2, operadores) {
    if (
        vetor1.length !== vetor2.length ||
        vetor1.length !== operadores.length ||
        vetor2.length !== operadores.length
    ) {
        console.log("Os vetores devem ter o mesmo tamanho.");
        return;
    }

    const resultado = [];

    for (let i = 0; i < vetor1.length; i++) {
        switch (operadores[i]) {
            case '+':
                resultado.push(vetor1[i] + vetor2[i]);
                break;
            case '-':
                resultado.push(vetor1[i] - vetor2[i]);
                break;
            case '*':
                resultado.push(vetor1[i] * vetor2[i]);
                break;
            case '/':
                if (vetor2[i] !== 0) {
                    resultado.push(vetor1[i] / vetor2[i]);
                } else {
                    console.log("Divisão por zero detectada. Ignorando operação.");
                    resultado.push(null);
                }
                break;
            default:
                console.log(`Operador inválido na posição ${i}. Ignorando operação.`);
                resultado.push(null);
        }
    }

    return resultado;
}

// Função para ler um vetor de inteiros
function lerVetor() {
    const vetor = [];

    for (let i = 0; i < 20; i++) {
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
const vetor1 = lerVetor();
const vetor2 = lerVetor();
const operadores = prompt("Informe 20 operadores (+, -, *, /) separados por espaço:").split(' ');

const resultadoOperacoes = realizarOperacoes(vetor1, vetor2, operadores);

console.log("Vetor 1:", vetor1);
console.log("Vetor 2:", vetor2);
console.log("Operadores:", operadores);
console.log("Resultados:", resultadoOperacoes);

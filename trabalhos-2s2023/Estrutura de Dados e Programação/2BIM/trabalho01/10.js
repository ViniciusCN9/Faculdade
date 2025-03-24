function calcularAcertos(gabarito, respostasAluno) {
    let acertos = 0;

    for (let i = 0; i < gabarito.length; i++) {
        if (gabarito[i] === respostasAluno[i]) {
            acertos++;
        }
    }

    return acertos;
}

function analisarProva(gabarito, numeroAlunos, cartoesRespostas) {
    const resultadosAlunos = [];

    for (let i = 0; i < numeroAlunos; i++) {
        const numeroAluno = cartoesRespostas[i][0];
        const respostasAluno = cartoesRespostas[i].slice(1); // Remove o número do aluno

        const acertos = calcularAcertos(gabarito, respostasAluno);

        resultadosAlunos.push({
            numeroAluno: numeroAluno,
            acertos: acertos,
            porcentagemAcertos: (acertos / gabarito.length) * 100,
        });
    }

    return resultadosAlunos;
}

// Exemplo de uso
const gabarito = ['A', 'B', 'C', 'D', 'E', 'A', 'B', 'C', 'D', 'E', 'A', 'B', 'C', 'D', 'E', 'A', 'B', 'C', 'D', 'E', 'A', 'B', 'C', 'D', 'E', 'A', 'B', 'C', 'D', 'E'];
const numeroAlunos = 3;
const cartoesRespostas = [
    [1, 'A', 'B', 'C', 'D', 'E', 'A', 'B', 'C', 'D', 'E', 'A', 'B', 'C', 'D', 'E', 'A', 'B', 'C', 'D', 'E', 'A', 'B', 'C', 'D', 'E', 'A', 'B', 'C', 'D', 'E'],
    [2, 'A', 'B', 'C', 'D', 'E', 'A', 'B', 'C', 'D', 'E', 'A', 'B', 'C', 'D', 'E', 'A', 'B', 'C', 'D', 'E', 'A', 'B', 'C', 'D', 'E', 'A', 'B', 'C', 'D', 'E'],
    [3, 'A', 'B', 'C', 'D', 'E', 'A', 'B', 'C', 'D', 'E', 'A', 'B', 'C', 'D', 'E', 'A', 'B', 'C', 'D', 'E', 'A', 'B', 'C', 'D', 'E', 'A', 'B', 'C', 'D', 'E']
];

const resultados = analisarProva(gabarito, numeroAlunos, cartoesRespostas);

console.log("Resultados dos Alunos:");
console.log(resultados);

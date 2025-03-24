const prompt = require('prompt-sync')()

// Inicializa a matriz que representa as poltronas, todas inicialmente vazias
const salaDeCinema = [
    Array(20).fill(false),
    Array(20).fill(false),
    Array(20).fill(false),
    Array(20).fill(false),
];

function exibirPoltronas() {
    console.log("Estado das Poltronas:");

    for (let i = 0; i < salaDeCinema.length; i++) {
        const fileira = String.fromCharCode(65 + i); // A, B, C, D para as fileiras

        for (let j = 0; j < salaDeCinema[i].length; j++) {
            const poltrona = j + 1;
            const estado = salaDeCinema[i][j] ? "Ocupada" : "Vazia";

            console.log(`Fileira ${fileira}, Poltrona ${poltrona}: ${estado}`);
        }
    }
}

function comprarIngresso() {
    const fileira = prompt("Informe a fileira (A, B, C, D):").toUpperCase();
    const poltrona = parseInt(prompt("Informe o número da poltrona (1-20):"));

    if (!["A", "B", "C", "D"].includes(fileira) || isNaN(poltrona) || poltrona < 1 || poltrona > 20) {
        console.log("Opção inválida. Tente novamente.");
        return;
    }

    const fileiraIndex = fileira.charCodeAt(0) - 65; // Convertendo A, B, C, D para índices 0, 1, 2, 3
    const poltronaIndex = poltrona - 1; // Ajustando para índices 0 a 19

    if (salaDeCinema[fileiraIndex][poltronaIndex]) {
        console.log("Esta poltrona já está ocupada. Escolha outra.");
        return;
    }

    salaDeCinema[fileiraIndex][poltronaIndex] = true;
    console.log(`Ingresso para Fileira ${fileira}, Poltrona ${poltrona} vendido com sucesso.`);
}

function exibirOcupacao() {
    let totalVazias = 0;
    let totalOcupadas = 0;

    for (let i = 0; i < salaDeCinema.length; i++) {
        for (let j = 0; j < salaDeCinema[i].length; j++) {
            if (salaDeCinema[i][j]) {
                totalOcupadas++;
            } else {
                totalVazias++;
            }
        }
    }

    console.log(`Total de Poltronas Vazias: ${totalVazias}`);
    console.log(`Total de Poltronas Ocupadas: ${totalOcupadas}`);
}

// Loop do menu
let opcao;

do {
    console.log("===== Menu de Opções =====");
    console.log("1. Exibir Poltronas");
    console.log("2. Comprar Ingresso");
    console.log("3. Exibir Ocupação");
    console.log("4. Sair");

    opcao = parseInt(prompt("Escolha uma opção (1-4):"));

    switch (opcao) {
        case 1:
            exibirPoltronas();
            break;
        case 2:
            comprarIngresso();
            break;
        case 3:
            exibirOcupacao();
            break;
        case 4:
            console.log("Saindo do programa. Até logo!");
            break;
        default:
            console.log("Opção inválida. Tente novamente.");
    }
} while (opcao !== 4);

const prompt = require('prompt-sync')()

class FilaAtendimento {
    constructor() {
        this.fila = [];
    }

    adicionarSolicitacao(cliente) {
        this.fila.push(cliente);
        console.log(`${cliente} adicionado à fila de atendimento.`);
    }

    atenderCliente() {
        if (this.fila.length > 0) {
            const clienteAtendido = this.fila.shift();
            console.log(`Atendendo ${clienteAtendido}.`);
        } else {
            console.log("Não há clientes na fila.");
        }
    }

    exibirFila() {
        console.log("Fila de Atendimento:");
        for (let i = 0; i < this.fila.length; i++) {
            console.log(`${i + 1}. ${this.fila[i]}`);
        }
    }
}

// Exemplo de uso
const filaAtendimento = new FilaAtendimento();

let opcao;

do {
    console.log("===== Menu de Atendimento =====");
    console.log("1. Adicionar Solicitação");
    console.log("2. Atender Cliente");
    console.log("3. Exibir Fila de Atendimento");
    console.log("4. Sair");

    opcao = parseInt(prompt("Escolha uma opção (1-4):"));

    switch (opcao) {
        case 1:
            const novaSolicitacao = prompt("Digite o nome do cliente:");
            filaAtendimento.adicionarSolicitacao(novaSolicitacao);
            break;
        case 2:
            filaAtendimento.atenderCliente();
            break;
        case 3:
            filaAtendimento.exibirFila();
            break;
        case 4:
            console.log("Encerrando atendimento. Até logo!");
            break;
        default:
            console.log("Opção inválida. Tente novamente.");
    }
} while (opcao !== 4);

const prompt = require('prompt-sync')()

class HistoricoNavegacao {
    constructor() {
        this.pilha = [];
    }

    empilhar(endereco) {
        this.pilha.push(endereco);
        console.log(`Navegando para: ${endereco}`);
    }

    desempilhar() {
        if (this.pilha.length > 1) {
            this.pilha.pop();
            console.log(`Voltando para: ${this.pilha[this.pilha.length - 1]}`);
        } else {
            console.log("Não há histórico para voltar.");
        }
    }

    exibirHistorico() {
        console.log("Histórico de Navegação:");
        for (let i = 0; i < this.pilha.length; i++) {
            console.log(`${i + 1}. ${this.pilha[i]}`);
        }
    }
}

const historico = new HistoricoNavegacao();

let opcao;

do {
    console.log("===== Menu de Navegação =====");
    console.log("1. Navegar para um novo endereço");
    console.log("2. Voltar para o endereço anterior");
    console.log("3. Exibir Histórico de Navegação");
    console.log("4. Sair");

    opcao = parseInt(prompt("Escolha uma opção (1-4):"));

    switch (opcao) {
        case 1:
            const novoEndereco = prompt("Digite o novo endereço:");
            historico.empilhar(novoEndereco);
            break;
        case 2:
            historico.desempilhar();
            break;
        case 3:
            historico.exibirHistorico();
            break;
        case 4:
            console.log("Saindo do programa. Até logo!");
            break;
        default:
            console.log("Opção inválida. Tente novamente.");
    }
} while (opcao !== 4);

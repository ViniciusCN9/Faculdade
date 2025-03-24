const { exit } = require('process');

const prompt = require('prompt-sync')()

class NoMenu {
    constructor(nome) {
        this.nome = nome;
        this.nosFilhos = [];
        this.noPai = null;
    }

    adicionarNoFilho(noFilho) {
        noFilho.noPai = this;
        this.nosFilhos.push(noFilho);
    }

    exibirMenu() {
        console.log(`===== Menu de Navegação - ${this.nome} =====`);
        console.log("9. Voltar ao Nó Anterior");
        console.log("0. Encerrar");

        for (let i = 0; i < this.nosFilhos.length; i++) {
            console.log(`${i + 1}. ${this.nosFilhos[i].nome}`);
        }
    }
}

// Criar a estrutura de árvore do menu
const menuPrincipal = new NoMenu("Principal");

const noticias = new NoMenu("Notícias");
const esportes = new NoMenu("Esportes");
const politica = new NoMenu("Política");

menuPrincipal.adicionarNoFilho(noticias);
menuPrincipal.adicionarNoFilho(esportes);
menuPrincipal.adicionarNoFilho(politica);

const noticiasNacionais = new NoMenu("Notícias Nacionais");
const noticiasInternacionais = new NoMenu("Notícias Internacionais");

noticias.adicionarNoFilho(noticiasNacionais);
noticias.adicionarNoFilho(noticiasInternacionais);

const futebol = new NoMenu("Futebol");
const basquete = new NoMenu("Basquete");
const tenis = new NoMenu("Tênis");

esportes.adicionarNoFilho(futebol);
esportes.adicionarNoFilho(basquete);
esportes.adicionarNoFilho(tenis);

const politicaNacional = new NoMenu("Política Nacional");
const politicaInternacional = new NoMenu("Política Internacional");

politica.adicionarNoFilho(politicaNacional);
politica.adicionarNoFilho(politicaInternacional);

// Interagir com o usuário usando prompts
let noAtual = menuPrincipal;

do {
    noAtual.exibirMenu();
    const opcao = parseInt(prompt("Escolha uma opção:"));

    switch (opcao) {
        case 9:
            // Voltar para o nó anterior
            if (noAtual.noPai !== null) {
                noAtual = noAtual.noPai;
                console.log(`Voltando para o nó anterior: ${noAtual.nome}`);
            } else {
                console.log("Você já está no menu principal.");
            }
            break;
        case 0:
            // Encerrar o programa
            console.log("Encerrando o programa. Até logo!");
            exit()
        default:
            // Navegar para o nó filho escolhido
            if (opcao > 0 && opcao <= noAtual.nosFilhos.length) {
                noAtual = noAtual.nosFilhos[opcao - 1];
            } else {
                console.log("Opção inválida. Tente novamente.");
            }
    }
} while (true); // Loop infinito até que o usuário decida encerrar

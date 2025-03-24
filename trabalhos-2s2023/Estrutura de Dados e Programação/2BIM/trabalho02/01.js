const prompt = require('prompt-sync')()

// Inicializa uma lista de compras vazia
const listaDeCompras = [];

// Função para adicionar itens à lista
function adicionarItem() {
    const novoItem = prompt("Digite o nome do produto para adicionar à lista:");
    if (novoItem) {
        listaDeCompras.push(novoItem);
        console.log(`${novoItem} foi adicionado à lista de compras.`);
    } else {
        console.log("Por favor, insira um nome de produto válido.");
    }
}

// Função para pesquisar e remover itens da lista
function pesquisarERemoverItem() {
    const itemParaRemover = prompt("Digite o nome do produto para pesquisar e remover:");
    const indiceItem = listaDeCompras.indexOf(itemParaRemover);

    if (indiceItem !== -1) {
        listaDeCompras.splice(indiceItem, 1);
        console.log(`${itemParaRemover} foi removido da lista de compras.`);
    } else {
        console.log(`${itemParaRemover} não foi encontrado na lista de compras.`);
    }
}

// Função para exibir a lista de compras
function exibirListaDeCompras() {
    console.log("Lista de Compras:");
    for (let i = 0; i < listaDeCompras.length; i++) {
        console.log(`${i + 1}. ${listaDeCompras[i]}`);
    }
}

// Loop do menu interativo
let opcao;

do {
    console.log("===== Menu de Compras =====");
    console.log("1. Adicionar Item");
    console.log("2. Pesquisar e Remover Item");
    console.log("3. Exibir Lista de Compras");
    console.log("4. Sair");

    opcao = parseInt(prompt("Escolha uma opção (1-4):"));

    switch (opcao) {
        case 1:
            adicionarItem();
            break;
        case 2:
            pesquisarERemoverItem();
            break;
        case 3:
            exibirListaDeCompras();
            break;
        case 4:
            console.log("Saindo do programa. Até logo!");
            break;
        default:
            console.log("Opção inválida. Tente novamente.");
    }
} while (opcao !== 4);

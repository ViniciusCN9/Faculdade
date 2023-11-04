def consolidar_pedidos(lista_pedidos):
    pedidos_consolidados = {}

    for pedido in lista_pedidos:
        cliente = pedido['cliente']
        produto = pedido['produto']
        quantidade = pedido['quantidade']

        if cliente in pedidos_consolidados:
            if produto in pedidos_consolidados[cliente]:
                pedidos_consolidados[cliente][produto] += quantidade
            else:
                pedidos_consolidados[cliente][produto] = quantidade
        else:
            pedidos_consolidados[cliente] = {produto: quantidade}

    return pedidos_consolidados


lista_de_pedidos = [
    {'cliente': 'Joao', 'produto': 'Camiseta', 'quantidade': 2},
    {'cliente': 'Maria', 'produto': 'Calça', 'quantidade': 1},
    {'cliente': 'Joao', 'produto': 'Camiseta', 'quantidade': 1},
    {'cliente': 'Maria', 'produto': 'Camiseta', 'quantidade': 3},
    {'cliente': 'Joao', 'produto': 'Boné', 'quantidade': 2},
    {'cliente': 'Maria', 'produto': 'Calça', 'quantidade': 2},
]

pedidos_consolidados = consolidar_pedidos(lista_de_pedidos)

for cliente, produtos in pedidos_consolidados.items():
    print(f"Cliente: {cliente}")
    for produto, quantidade in produtos.items():
        print(f"Produto: {produto}, Quantidade: {quantidade}")
    print("------")

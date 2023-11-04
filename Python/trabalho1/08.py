def resumo_produtos(precos, estoque):
    produtos = {}
    for produto in set(precos.keys()) | set(estoque.keys()):
        produtos[produto] = {
            'preco': precos.get(produto, 'Preço não disponível'),
            'quantidade': estoque.get(produto, 'Quantidade não disponível')
        }
    return produtos


precos = {
    'banana': 2.5,
    'maçã': 1.8,
    'laranja': 2.0
}
estoque = {
    'banana': 10,
    'maçã': 15,
    'uva': 8
}
resumo = resumo_produtos(precos, estoque)

for produto, info in resumo.items():
    print(
        f"Produto: {produto}, Preço: {info['preco']}, Quantidade: {info['quantidade']}")

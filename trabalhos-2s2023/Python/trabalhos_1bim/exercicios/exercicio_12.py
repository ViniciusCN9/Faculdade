estoque = []
total_estoque = 0

while True:
    opcao = input("Escolha uma opção (adicionar/listar/sair): ")

    if opcao == "sair":
        break
    elif opcao == "adicionar":
        nome = input("Digite o nome do produto: ")
        preco = float(input("Digite o preço do produto: "))
        quantidade = int(input("Digite a quantidade em estoque: "))
        produto = (nome, preco, quantidade)
        estoque.append(produto)
        total_estoque += (preco * quantidade)
    elif opcao == "listar":
        for nome, preco, quantidade in estoque:
            print(f"Produto: {nome}, Preço: {preco}, Quantidade: {quantidade}")
        print(f"Valor total do estoque: {total_estoque:.2f}")

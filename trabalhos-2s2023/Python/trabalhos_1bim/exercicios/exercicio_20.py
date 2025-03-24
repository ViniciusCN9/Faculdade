compras = {}
total = 0

while True:
    produto = input("Digite o nome do produto (ou 'sair' para encerrar): ")

    if produto == "sair":
        break
    elif produto in compras:
        quantidade = int(input("Digite a quantidade comprada: "))
        compras[produto]['quantidade'] += quantidade
    else:
        preco = float(input("Digite o preço do produto: "))
        quantidade = int(input("Digite a quantidade comprada: "))
        compras[produto] = {'preco': preco, 'quantidade': quantidade}
        
    total += preco * quantidade

print("\nLista de Compras:")
for produto, info in compras.items():
    preco_unitario = info['preco']
    quantidade = info['quantidade']
    preco_total = preco_unitario * quantidade
    print(f"{produto}: {quantidade} unidades X R${preco_unitario:.2f} cada = R${preco_total:.2f}")

print(f"Total a pagar: R${total:.2f}")
agenda = {}

while True:
    opcao = input("Escolha uma opcao (adicionar/consultar/listar/sair): ")

    if opcao == "sair":
        break
    elif opcao == "adicionar":
        nome = input("Digite o nome do contato: ")
        telefone = input("Digite o número do telefone: ")
        agenda[nome] = telefone
    elif opcao == "consultar":
        nome = input("Digite o nome do contato para consultar o telefone: ")
        if nome in agenda:
            print(f"O número de telefone de {nome} é {agenda[nome]}")
        else:
            print(f"{nome} não encontrado.")
    elif opcao == "listar":
        for nome, telefone in agenda.items():
            print(f"{nome}: {telefone}")

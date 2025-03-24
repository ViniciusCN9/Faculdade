alunos = {}

while True:
    opcao = input("Escolha uma opção (adicionar/consultar/media/sair): ")

    if opcao == "sair":
        break
    elif opcao == "adicionar":
        nome = input("Digite o nome do aluno: ")
        nota = float(input("Digite a nota do aluno: "))
        alunos[nome] = nota
    elif opcao == "consultar":
        nome = input("Digite o nome do aluno para consultar a nota: ")
        if nome in alunos:
            print(f"A nota de {nome} é {alunos[nome]:.2f}")
        else:
            print(f"{nome} não encontrado.")
    elif opcao == "media":
        if len(alunos) == 0:
            print("Nenhum aluno cadastrado.")
        else:
            media = sum(alunos.values()) / len(alunos)
            print(f"Média das notas dos alunos: {media:.2f}")
import os
import time

def limpar():
    print("\n" * os.get_terminal_size().lines)

def carregando():
    limpar()
    print("Carregando o sistema .")
    time.sleep(1)
    limpar()
    print("Carregando o sistema ..")
    time.sleep(1)
    limpar()
    print("Carregando o sistema ...")
    time.sleep(1)

def saudacao():
    limpar()
    print("========================================================")
    print("Bem vindo ao sistema educacional da faculdade Gran Tietê")
    print("========================================================\n")

def opcaoInvalida():
    print("\nOpção inválida!")
    time.sleep(2)
    limpar()

def opcoes():
    print("Informe a ação desejada:")
    print("1 - Consultar alunos cadastrados")
    print("2 - Consultar informações de aluno")
    print("3 - Adicionar novo aluno")
    print("4 - Atualizar informações dos alunos")
    print("5 - Deletar aluno cadastrado")
    print("0 - Sair\n")

    try:
        opcao = int(input("Opção: "))
        limpar()
    except:
        opcaoInvalida()
        opcoes()

    match opcao:
        case 1:
            print("")
            opcoes()
        case 2:
            print("2")
            opcoes()
        case 3:
            print("3")
            opcoes()
        case 4:
            print("4")
            opcoes()
        case 5:
            print("5")
            opcoes()
        case 0:
            print("0")
        case _:
            opcaoInvalida()
            opcoes()

def main():
    carregando()
    saudacao()
    opcoes()

main()
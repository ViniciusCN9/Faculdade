import os
import time
from faculdade import Faculdade
from aluno import Aluno
from curso import Curso

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

def encerrando():
    limpar()
    print("Encerrando .")
    time.sleep(1)
    limpar()
    print("Encerrando ..")
    time.sleep(1)
    limpar()
    print("Encerrando ...")
    time.sleep(1)
    limpar()

def saudacao():
    limpar()
    print("========================================================")
    print("Bem vindo ao sistema educacional da faculdade Gran Tietê")
    print("========================================================\n")

def opcaoInvalida(mensagem = "Opção inválida!"):
    print(f"\n{mensagem}")
    time.sleep(2)
    limpar()

def sucesso(mensagem = "Operação realizada com sucesso!"):
    print(f"\n{mensagem}")
    time.sleep(2)
    limpar()

def listarAluno():
    while True:
        print("Consultar informações de aluno\n")

        try:
            id = int(input("Informe o ID do aluno: "))
            break
        except:
            opcaoInvalida("Id informado inválido")

    limpar()
    Faculdade.listarAluno(id)

def adicionarAluno():
    while True:
        print("Adicionar novo aluno\n")

        Faculdade.listarCursos()

        nome = input("\nInforme o nome do aluno: ")
        try: 
            curso = int(input("Informe o curso do aluno: "))
            if (curso in Faculdade.cursos.keys()):
                break
            else:
                opcaoInvalida("Curso não disponível na faculdade!")
        except:
            opcaoInvalida()
    
    aluno = Aluno(nome, Curso(curso))
    Faculdade.adicionarAluno(aluno)
    sucesso()

def atualizarAluno():
    while True:
        print("Atualizar informações dos alunos\n")

        try:
            id = int(input("Informe o ID do aluno: "))
            aluno = Faculdade.listarAluno(id)
            if not aluno:
                time.sleep(2)
                return
        except:
            opcaoInvalida("Id informado inválido")
            return

        print("\n")
        Faculdade.listarCursos()
        
        nome = input("\nInforme o novo nome do aluno: ")
        try:
            curso = int(input("Informe o novo curso do aluno: "))
            if (curso in Faculdade.cursos.keys()):
                break
            else:
                opcaoInvalida("Curso não disponível na faculdade!")
        except:
            opcaoInvalida()
    
    Faculdade.atualizarAluno(id, nome, Curso(curso))
    sucesso()

def removerAluno():
    while True:
        print("Deletar aluno cadastrado\n")

        try:
            id = int(input("Informe o ID do aluno: "))
            aluno = Faculdade.listarAluno(id)
            if not aluno:
                time.sleep(2)
                return
        except:
            opcaoInvalida("Id informado inválido")
            return

        try:
            confirma = input("\nConfirma a remoção do aluno? (S/N): ")
            if (confirma.upper() == "S"):
                break
            elif (confirma.upper() == "N"):
                opcaoInvalida("Operação cancelada!")
                return
            else:
                opcaoInvalida()
        except:
            opcaoInvalida()
    
    Faculdade.removerAluno(id)
    sucesso()

def opcoes():
    saudacao()
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

    """"
    # Opção para versoões superiores à python 3.10
    match opcao:
        case 1:
            Faculdade.listarAlunos()
            input("\n Aperte qualquer tecla para voltar")
            limpar()
            opcoes()
        case 2:
            listarAluno()
            input("\n Aperte qualquer tecla para voltar")
            limpar()
            opcoes()
        case 3:
            adicionarAluno()
            opcoes()
        case 4:
            atualizarAluno()
            opcoes()
        case 5:
            removerAluno()
            opcoes()
        case 0:
            pass
        case _:
            opcaoInvalida()
            opcoes()
    """

    if (opcao == 1):
        Faculdade.listarAlunos()
        input("\n Aperte qualquer tecla para voltar")
        limpar()
        opcoes()
    elif (opcao == 2):
        listarAluno()
        input("\n Aperte qualquer tecla para voltar")
        limpar()
        opcoes()
    elif (opcao == 3):
        adicionarAluno()
        opcoes()
    elif (opcao == 4):
        atualizarAluno()
        opcoes()
    elif (opcao == 5):
        removerAluno()
        opcoes()
    elif (opcao == 0):
        pass
    else:
        opcaoInvalida()
        opcoes()
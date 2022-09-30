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

def adicionarAluno():
    print("Adicionar novo aluno\n")

    nome = input("Informe o nome do aluno: ")
    while True:
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

def listarAluno():
    print("Consultar informações de aluno\n")

    while True:
        try:
            id = int(input("Informe o ID do aluno: "))
            break
        except:
            opcaoInvalida("Id informado inválido")

    Faculdade.listarAluno(id)

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
            print("Ainda não implementado")
            opcoes()
        case 5:
            print("Ainda não implementado")
            opcoes()
        case 0:
            encerrando()
        case _:
            opcaoInvalida()
            opcoes()

def main():
    carregando()
    saudacao()
    opcoes()

main()
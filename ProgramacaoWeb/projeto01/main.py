import os
import time
from funcionario import funcionario

def main():
    funcionarios = []

    print("BEM VINDO")
    print("Carregando...")
    time.sleep(5)
    def menu():
        print("\n" * os.get_terminal_size().lines)
        print("Digite 1 para adicionar um funcionário")
        print("Digite 2 para listar funcionários")
        print("Digite 0 para sair")

        opcao = input()
        match opcao:
            case "1":
                adicionar()
                menu()
            case "2":
                listar()
                input("Digite qualquer tecla para voltar")
                menu()
            case _:
                print("\n" * os.get_terminal_size().lines)
                print("Obrigado!")
                return

    def adicionar():
        print("\n" * os.get_terminal_size().lines)
        nome = input("Digite o nome: ")
        sobrenome = input("Digite o sobrenome: ")
        emprego = input("Digite o emprego: ")
        salario = float(input("Digite o salário: "))
        funcionarios.append(funcionario(nome=nome, sobrenome=sobrenome, emprego=emprego, salario=salario))

        print("\n" * os.get_terminal_size().lines)
        print("Funcionário adicionado com sucesso!")
        time.sleep(2)

    def listar():
        print("\n" * os.get_terminal_size().lines)
        if len(funcionarios) == 0:
            print("Nenhum funcionário cadastrado!")
            return

        for funcionario in funcionarios:
            funcionario.exibir()

    menu()
main()
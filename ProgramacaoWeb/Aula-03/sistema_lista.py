import os

lista = []

def main():
    print("\n" * os.get_terminal_size().lines)
    print(f"LISTA: {lista}")
    print("ESCOLHA A OPÇÃO:")
    print("1 - ADICIONAR NÚMERO")
    print("2 - REMOVER NÚMERO")
    print("0 - SAIR")

    opcao = int(input())
    
    match opcao:
        case 1:
            adicionar()
            main()
        case 2:
            remover()
            main()
        case 0:
            print("\n" * os.get_terminal_size().lines)
            return

def adicionar():
    lista.append(int(input("Digite o valor: ")))

def remover():
    del lista[int(input("Digite a posição do valor que deseja remover: "))]

main()


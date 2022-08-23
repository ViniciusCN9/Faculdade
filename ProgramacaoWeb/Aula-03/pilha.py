import os
import time

fila = ["A", "B", "C", "D", "E", "F", "G"]

def main():
    print("\n" * os.get_terminal_size().lines)
    print(f"FILA: {fila}")
    print("ESCOLHA A OPÇÃO:")
    print("1 - ADICIONAR PESSOA")
    print("2 - ATENDER")
    print("0 - SAIR")

    opcao = int(input())
    
    match opcao:
        case 1:
            adicionar()
            main()
        case 2:
            atender()
            main()
        case 0:
            print("\n" * os.get_terminal_size().lines)
            return

def adicionar():
    fila.append((input("INFORME NOME DA PESSOA: ").upper()))

def atender():
    if (len(fila) == 0):
        print("FILA VAZIA!")
        time.sleep(2)
        return

    print(f"ATENDENDO PESSOA: {fila[-1]} ...")
    time.sleep(2)
    fila.pop(-1)

main()
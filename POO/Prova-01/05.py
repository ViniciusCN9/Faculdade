def exibirMultiplos():
    multiplos = []

    for valor in range(1000):
        if (valor % 3 == 0 and valor % 5 == 0):
            multiplos.append(valor)

    print(f"A soma é de: {sum(multiplos)}") 

print("Soma dos múltiplos de 3 e 5 abaixo de 1000")
exibirMultiplos()
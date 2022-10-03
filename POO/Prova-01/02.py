def exibirMultiplos():
    multiplos = []

    for valor in range(10, 50):
        if (valor % 3 == 0):
            multiplos.append(valor)

    print(multiplos)

print("Múltiplos de 3 entre 10 e 50")
exibirMultiplos()
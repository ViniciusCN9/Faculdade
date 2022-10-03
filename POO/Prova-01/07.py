def exibirMaior(valorA, valorB, valorC):
    valores = [valorA, valorB, valorC]
    print(f"O maior valor é : {max(valores)}")

print("O maior entre 3 valores")
valorA = int(input("Insira o primeiro valor: "))
valorB = int(input("Insira o segundo valor: "))
valorC = int(input("Insira o terceiro valor: "))
exibirMaior(valorA, valorB, valorC)
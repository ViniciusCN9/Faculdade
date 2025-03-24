entrada = input("Digite uma lista de números separados por espaço: ")
numeros = [float(numero) for numero in entrada.split()]

numeros.sort()

print("Lista de classificada em ordem crescente: ")
print(numeros)
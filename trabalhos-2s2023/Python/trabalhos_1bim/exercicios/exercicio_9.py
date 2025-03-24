entrada = input("Digite uma lista de números separados por espaço: ")
numeros = [int(numero) for numero in entrada.split()]

soma = 0
for numero in numeros:
    if numeros.count(numero) == 1:
        soma += numero

print("Soma dos números únicos na lista:", soma)
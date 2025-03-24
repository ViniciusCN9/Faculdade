entrada = input("Digite uma lista de números separados por espaço: ")
numeros = [int(numero) for numero in entrada.split()]

contagem = {}
for numero in numeros:
    if numeros.count(numero) > 1:
        contagem[numero] = numeros.count(numero)

    
for numero, quantidade in contagem.items():
    print(f"{numero} aparece {quantidade} vezes.")
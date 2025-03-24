entrada = input("Digite uma lista de números separados por espaço: ")
numeros = [float(numero) for numero in entrada.split()]

numeros.sort()
menores = numeros[:2]
maiores = numeros[-2:]

media_menores = sum(menores) / len (menores)
media_maiores = sum(maiores) / len(maiores)

print(f"Média dos dois menores números: {media_menores:.2f}")
print(f"Média dos dois maiores números: {media_maiores:.2f}")


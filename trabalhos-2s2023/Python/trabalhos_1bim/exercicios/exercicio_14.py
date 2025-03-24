elementos = [1, 2, 2, 3, 4, 4, 4, 5, 5]

contagem = {}
for elemento in elementos:
    if elemento in contagem:
        contagem[elemento] += 1
    else:
        contagem[elemento] = 1

for elemento, quantidade in contagem.items():
    print(f"{elemento}: {quantidade} vezes")
    
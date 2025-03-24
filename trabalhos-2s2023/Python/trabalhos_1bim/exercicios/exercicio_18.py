palavra = input("Digite uma palavra: ")
contagem = {}

for letra in palavra:
    letra = letra.lower()
    if letra in contagem:
        contagem[letra] += 1
    else:
        contagem[letra] = 1

for letra, quantidade in contagem.items():
    print(f"'{letra}': {quantidade} vezes")
frase = input("Digite uma frase: ")
palavras = frase.split()
contagem = {}

for palavra in palavras:
    palavra = palavra.lower()
    if palavra in contagem:
        contagem[palavra] += 1
    else:
        contagem[palavra] = 1

for palavra, quantidade in contagem.items():
    print(f"'{palavra}'; {quantidade} vezes")
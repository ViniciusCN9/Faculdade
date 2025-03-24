frase = input("Digite uma frase: ")
palavras = frase.split()
palavras_unicas = list(set(palavras))
palavras_unicas.sort()

print("Palavras únicas em ordem alfabética: ")
print(" ".join(palavras_unicas))

entrada = input("Digite uma lista de palavras separadas por espaço: ")
palavras = entrada.split()

def e_palindromo(palavra):
    return palavra == palavra[::-1]

for palavra in palavras:
    if e_palindromo(palavra):
        print(f"{palavra} é um palíndromo.")
    else:
        print(f"{palavra} não é um palíndromo.")
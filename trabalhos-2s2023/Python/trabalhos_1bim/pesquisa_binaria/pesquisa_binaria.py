import random 

def busca_binaria(lista, valor):
    esquerda, direita = 0, len(lista) - 1
    tentativas = 0

    while esquerda <= direita:
        tentativas += 1
        meio = (esquerda + direita) // 2
        if lista[meio] == valor:
            return meio, tentativas
        elif lista[meio] < valor:
            esquerda = meio + 1
        else:
            direita = meio - 1
    return -1, tentativas
lista = sorted(random.sample(range(0, 1001), 500))
# lista = [i for i in range(0, 11)]

print("Lista de números:")
print(lista)

valor = int(input("\nDigite um número entre 0 e 1.000 para buscar: "))

posicao, tentativas = busca_binaria(lista, valor)

if posicao != -1:
    print(f"\nO número {valor} foi encontrado na posição {posicao + 1}.")
    print(f"Foram necesssárias {tentativas} tentativas para encontrar o número")
else:
    print(f"\nO número {valor} não foi encontrado.")
    print(f"Foram realizadas {tentativas} tentativas.")
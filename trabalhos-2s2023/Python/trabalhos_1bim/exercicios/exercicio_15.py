lista1 = ["a", "b", "c"]
lista2 = [1, 2, 3]

tuplas_combinadas = [(elem1, elem2) for elem1, elem2 in zip(lista1, lista2)]

for tupla in tuplas_combinadas:                      
    print(tupla)
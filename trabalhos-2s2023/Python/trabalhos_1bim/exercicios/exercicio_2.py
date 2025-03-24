matriz_multiplicacao = []

for i in range(1, 6):
    linha = []
    for j in range(1, 6):
        resultado = i * j
        linha.append(resultado)
    matriz_multiplicacao.append(linha)

for linha in matriz_multiplicacao:
    print(linha)



        
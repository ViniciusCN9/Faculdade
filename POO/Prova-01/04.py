print("Valores decrescentes a partir da entrada informada")

while True:
    MINIMO = 50
    MAXIMO = 100

    entrada = int(input("Digite um número entre 50 e 100: "))
    if (entrada > MINIMO and entrada < MAXIMO):
        break
    else:
        print("Valor inválido!")

valores = []
for i in range(entrada, -1, -1):
    valores.append(i)

print(valores)
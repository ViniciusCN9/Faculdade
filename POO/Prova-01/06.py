import random

listaA = []
listaB = []

for i in range(100):
    numeroAleatorio = random.randint(0, 1000)
    listaA.append(numeroAleatorio)

print("Números aleatórios")
print(listaA)

for numero in listaA:
    if (not numero % 2 == 0):
        listaB.append(numero)

print("\nNúmeros aleatórios que não são múltiplos de 2")
print(listaB)




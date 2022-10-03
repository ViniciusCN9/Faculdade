import random

listaA = []
listaB = []

for i in range(50):
    numeroAleatorio = random.randint(0, 101)
    listaA.append(numeroAleatorio)

for numero in listaA:
    if (sum(int(algarismo) for algarismo in str(numero)) % 2 == 0):
        listaB.append(numero)

print("Números aleatórios cujo a soma de seus algarismos é par")
print(listaB)


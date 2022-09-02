# firstValue = int(input("Digite o primeiro valor inteiro: "))
# secondValue =int(input("Digite o segundo valor inteiro: "))
# thirdValue = int(input("Digite o terceiro valor inteiro: "))

# print(f"A soma dos valores inteiros é: {firstValue + secondValue + thirdValue}")

sumNumbers = 0

for i in range(3):
    number = int(input("Digite um valor inteiro: "))
    sumNumbers += number

print(f"A soma dos valores inteiros é: {sumNumbers}")


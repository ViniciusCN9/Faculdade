def convertDegreesToRad(value):
    return value * (3.14 / 180)

angleDegrees = float(input("Informe o ângulo em graus: "))
print(f"O ângulo em radianos é de : %.2f" % (convertDegreesToRad(angleDegrees)))
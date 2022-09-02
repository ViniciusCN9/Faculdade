def convertRadToDegrees(value):
    return value * (180 / 3.14)

angleRad = float(input("Informe o ângulo em radianos: "))
print(f"O ângulo em graus é de : %.1f°" % (convertRadToDegrees(angleRad)))
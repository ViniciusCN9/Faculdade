def convertCubicMetersToLiters(value):
    return value * 1000

volumeCubicMeters = float(input("Informe o volume em m³: "))
print(f"O volume em litros é de : %.1fL" % (convertCubicMetersToLiters(volumeCubicMeters)))
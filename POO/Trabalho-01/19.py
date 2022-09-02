def convertLitersToCubicMeters(value):
    return value / 1000

volumeLiters = float(input("Informe o volume em litros: "))
print(f"O volume em m³ é de : %.1f" % (convertLitersToCubicMeters(volumeLiters)))
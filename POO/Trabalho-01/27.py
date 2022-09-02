def convertHectaresToSquareMeters(value):
    return value * 10000

areaHectares = float(input("Informe a área em hectares: "))
print(f"A área em m² é de : %.1f" % (convertHectaresToSquareMeters(areaHectares)))
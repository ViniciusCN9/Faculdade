def convertSquareMetersToAcres(value):
    return value * 0.000247

areaSquareMeters = float(input("Informe a área em m²: "))
print(f"A área em acres é de : %.1f" % (convertSquareMetersToAcres(areaSquareMeters)))
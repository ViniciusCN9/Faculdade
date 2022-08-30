def convertSquareMetersToHectares(value):
    return value * 0.0001

areaSquareMeters = float(input("Informe a área em m²: "))
print(f"A área em hectares é de : %.1f" % (convertSquareMetersToHectares(areaSquareMeters)))
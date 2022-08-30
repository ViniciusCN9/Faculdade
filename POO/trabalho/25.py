def convertAcresToSquareMeters(value):
    return value * 4048.58

areaAcres = float(input("Informe a área em acres: "))
print(f"A área em m² é de : %.1f" % (convertAcresToSquareMeters(areaAcres)))
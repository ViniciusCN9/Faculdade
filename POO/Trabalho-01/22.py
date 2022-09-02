def convertMeterToYardss(value):
    return value * 0.91

distanceMeters = float(input("Informe a distância em metros: "))
print(f"A distância em jardas é de : %.1f" % (convertMeterToYardss(distanceMeters)))
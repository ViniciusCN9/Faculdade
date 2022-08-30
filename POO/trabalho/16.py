def convertInchesToCentimeters(value):
    return value * 2.54

distanceInches = float(input("Informe a distância em polegadas: "))
print(f"A distância em centimetros é de : %.2f" % (convertInchesToCentimeters(distanceInches)))
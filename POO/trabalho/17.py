def convertCentimetersToInches(value):
    return value / 2.54

distanceCentimeters = float(input("Informe a distância em centimetros: "))
print(f"A distância em polegadas é de : %.1f" % (convertCentimetersToInches(distanceCentimeters)))
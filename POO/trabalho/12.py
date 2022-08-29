def convertQuilometersToMiles(value):
    return 1.61 * value

distanceMiles = float(input("Informe a distância em milhas: "))
print(f"A distância em quilometros é de : %.1f" % (convertQuilometersToMiles(distanceMiles)))
def convertMilesToQuilometers(value):
    return value / 1.61

distanceMiles = float(input("Informe a distância em quilometros: "))
print(f"A distância em milhas é de : %.1f" % (convertMilesToQuilometers(distanceMiles)))
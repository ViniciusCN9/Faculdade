def convertYardsToMeters(value):
    return value / 0.91

distanceYards = float(input("Informe a distância em jardas: "))
print(f"A distância em metros é de : %.1f" % (convertYardsToMeters(distanceYards)))
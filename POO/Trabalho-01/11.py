def convertMTSToKMH(value):
    return value * 3.6

speedMTS = float(input("Informe a velocidade em m/s: "))
print(f"A velocidade em Km/h é de: %.1f" % (convertMTSToKMH(speedMTS)))

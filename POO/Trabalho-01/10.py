def convertKMHToMTS(value):
    return value / 3.6

speedKMH = float(input("Informe a velocidade em Km/h: "))
print(f"A velocidade em m/s é de: %.1f" % (convertKMHToMTS(speedKMH)))
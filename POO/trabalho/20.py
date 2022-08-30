def convertKilogramsToPounds(value):
    return value / 0.45

massKilogram = float(input("Informe a massa em quilogramas: "))
print(f"A massa em libras é de : %.1f" % (convertKilogramsToPounds(massKilogram)))
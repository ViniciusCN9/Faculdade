def convertPoundsToKilograms(value):
    return value * 0.45

massPounds = float(input("Informe a massa em libras: "))
print(f"A massa em quilogramas é de : %.1f" % (convertPoundsToKilograms(massPounds)))
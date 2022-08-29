def convertCelciusToKelvin(value):
    return value + 273.15

temperatureCelsius = float(input("Digite a temperatura em Celsius: "))
print(f"O valor em Kelvin é de: %.1fK" % (convertCelciusToKelvin(temperatureCelsius)))
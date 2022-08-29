def convertCelsiusToFahrenheit(value):
    return value * (9/5) + 32

temperatureCelsius = float(input("Digite a temperatura em graus Celsius: "))
print(f"O valor em fahrenheit é de: %.1f°F" % (convertCelsiusToFahrenheit(temperatureCelsius)))




def convertFahrenheitToCelcius(value):
    return 5 * (value - 32) / 9

temperatureFahrenheit = float(input("Digite a temperatura em graus Fahrenheit: "))
print(f"O valor em Celsius é de: %.1f°C" % (convertFahrenheitToCelcius(temperatureFahrenheit)))
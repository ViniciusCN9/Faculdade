def convertKelvinToCelcius(value):
    return value - 273.15

temperatureKelvin = float(input("Digite a temperatura em Kelvin: "))
print(f"O valor em Celsius é de: %.1f°C" % (convertKelvinToCelcius(temperatureKelvin)))
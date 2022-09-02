def convertRealToDollar(value, price):
    return value / price

valueReal = float(input("Informe o valor em Reais(R$): "))
priceDollar = float(input("Informe a cotação atual do Dollar($): "))
print(f"A conversão em dolares é de: %.2f$" % (convertRealToDollar(valueReal, priceDollar)))
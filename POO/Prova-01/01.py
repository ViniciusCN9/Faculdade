def calcularRendimento(tamanho, litrosLata = 18, precoReais = 200):
    litrosUtilizados = tamanho / 3
    latasUtilizadas = int(litrosUtilizados / litrosLata)
    
    if (litrosUtilizados % litrosLata == 0):
        precoTotal = latasUtilizadas * precoReais
        print(f"Serão necessários {latasUtilizadas} latas de tinta, no valor de R$ %.2f" % (precoTotal))
    else:
        precoTotal = (latasUtilizadas + 1) * precoReais
        print(f"Serão necessários {int(latasUtilizadas + 1)} latas de tinta, no valor de R$ %.2f" % (precoTotal))

print("Loja de Tintas")
tamanho = float(input("Informe o tamanho a ser pintado em m²: "))
calcularRendimento(tamanho)
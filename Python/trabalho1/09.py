def melhor_mes(vendas):
    mes_mais_vendas = max(vendas, key=vendas.get)
    vendas_mais_altas = vendas[mes_mais_vendas]
    return (mes_mais_vendas, vendas_mais_altas)


vendas = {
    'Janeiro': 15000,
    'Fevereiro': 22000,
    'Março': 18000,
    'Abril': 25000,
    'Maio': 21000
}

melhor = melhor_mes(vendas)

print(
    f"O mês com mais vendas foi {melhor[0]} com um total de vendas de {melhor[1]}")

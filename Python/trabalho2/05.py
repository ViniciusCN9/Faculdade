import pandas as pd

# Carregar o dataset
data = pd.read_csv('billions.csv')

# 1. Liste as top 5 categorias com o maior número de bilionários.
top_5_categorias = data['category'].value_counts().head(5)
print("Top 5 categorias com o maior número de bilionários:")
print(top_5_categorias)

# 2. Qual é o patrimônio líquido médio dos bilionários em cada uma dessas categorias?
print("\nPatrimônio líquido médio por categoria:")
for categoria in top_5_categorias.index:
    media = data[data['category'] == categoria]['finalWorth'].mean()
    print(f" {categoria}: ${media:.2f} bilhões")

# 3. Análise de Idade:
idade_media = data['age'].mean()
idade_maxima = data['age'].max()
idade_minima = data['age'].min()
print(f"\nIdade média dos bilionários: {idade_media:.2f} anos")
print(f"Idade do bilionário mais velho: {idade_maxima} anos")
print(f"Idade do bilionário mais jovem: {idade_minima} anos")

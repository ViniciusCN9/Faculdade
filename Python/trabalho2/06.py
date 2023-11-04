import pandas as pd

# Carregar o dataset
data = pd.read_csv('billions.csv')

# 1. Qual é a idade média dos bilionários?
idade_media = data['age'].mean()
print(f"Idade média dos bilionários: {idade_media:.2f} anos")

# 2. Quem é o bilionário mais jovem e o mais velho?
bilionario_mais_jovem = data[data['age'] == data['age'].min()]
bilionario_mais_velho = data[data['age'] == data['age'].max()]
print(
    f"\nBilionário mais jovem: {bilionario_mais_jovem['personName'].values[0]} com {bilionario_mais_jovem['age'].values[0]} anos")
print(
    f"Bilionário mais velho: {bilionario_mais_velho['personName'].values[0]} com {bilionario_mais_velho['age'].values[0]} anos")

# 3. Bilionários por Gênero:
distribuicao_genero = data['gender'].value_counts()
print("\nDistribuição de bilionários por gênero: ")
print(distribuicao_genero.to_string())

import pandas as pd


# Carregar o dataset
data = pd.read_csv('billions.csv')

# 1. Carregue o dataset e exiba as primeiras 5 linhas.
print(data.head())

# 2. Liste todas as colunas do dataset.
print(data.columns)

# 3. Mostre as informações básicas do dataset.
print(data.info())

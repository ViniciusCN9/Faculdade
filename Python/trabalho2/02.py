import pandas as pd

# Carregar o dataset
data = pd.read_csv('billions.csv')

# Média do patrimônio líquido
media = data['finalWorth'].mean()
print(f'Média do Patrimônio Líquido: ${media:.2f} bilhões')

# Mediana do patrimônio líquido
mediana = data['finalWorth'].median()
print(f'Mediana do Patrimônio Líquido: ${mediana: .2f} bilhões')

# Máximo patrimônio líquido
maximo = data['finalWorth'].max()
print(f' Máximo Patrimônio Líquido: ${maximo:.2f} bilhões')

# Mínimo patrimônio líquido
minimo = data['finalWorth'].min()
print(f'Mínimo Patrimônio Líquido: ${minimo:.2f} bilhões')

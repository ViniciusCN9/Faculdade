import pandas as pd

pd.set_option('display.max_rows', None)

# Carregar o dataset
data = pd.read_csv('billions.csv')

# Selecione bilionários da indústria tecnológica
tecnologia_bilionarios = data[(data['source'].str.contains('tech', case=False, na=False)) | (
    data['industries'].str.contains('tech', case=False, na=False))]
print("Bilionários que fizeram sua fortuna na indústria tecnológica: ")
print(tecnologia_bilionarios[['personName', 'country', 'finalWorth']])

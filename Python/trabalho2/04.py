import pandas as pd

# Carregar o dataset
data = pd.read_csv('billions.csv')
print(data['selfMade'].dtype)
print(data['selfMade'].value_counts())

self_made_count = data[data['selfMade'] == True].shape[0]
print(f'Número de bilionários "self-made": {self_made_count}')

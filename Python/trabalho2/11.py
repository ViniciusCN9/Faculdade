
import pandas as pd

pd.set_option('display.max_rows', None)

# Carregar o dataset
data = pd.read_csv('billions.csv')

# Converter a coluna birthDate para o formato de data
data['birthDate'] = pd.to_datetime(data['birthDate'], errors='coerce')

# Filtrar os bilionários que fazem aniversário em janeiro
aniversariantes_janeiro = data[data['birthDate'].dt.month == 1]
print("Bilionários que fazem aniversário em janeiro: ")
print(aniversariantes_janeiro[['personName', 'birthDate']])

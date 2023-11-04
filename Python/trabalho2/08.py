import pandas as pd
from datetime import datetime

# Carregue o dataset (ajuste o nome do arquivo conforme necessário)
data = pd.read_csv('billions.csv')

# Converta a coluna 'birthDate' para o tipo datetime
data['birthDate'] = pd.to_datetime(data['birthDate'], errors='coerce')

# Calcule a idade com base na data de nascimento
current_year = datetime.now().year
data['age'] = current_year - data['birthDate'].dt.year

# Crie uma nova coluna 'age_group' para classificar os bilionários
data['age_group'] = pd.cut(data['age'], bins=[0, 40, 70, 150], labels=[
                           'Young', 'Middle-Aged', 'Senior'])

# Calcule o número total de bilionários em cada faixa etária
age_group_count = data['age_group'].value_counts()
print(age_group_count)

# Identifique os setores com o maior número de bilionários jovens
young_billionaires = data[data['age_group'] == 'Young']
young_by_industry = young_billionaires['industries'].value_counts().head(
    5)  # Top 5 setores
print("\nTop 5 setores com maior número de bilionários jovens :")
print(young_by_industry)

# Identifique os setores com o maior número de bilionários idosos.
senior_billionaires = data[data['age_group'] == 'Senior']
senior_by_industry = senior_billionaires['industries'].value_counts().head(
    5)  # Top 5 setores
print("\nTop 5 setores com maior número de bilionários idosos:")
print(senior_by_industry)

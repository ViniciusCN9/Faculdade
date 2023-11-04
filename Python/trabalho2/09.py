import pandas as pd

# Carregar o dataset
data = pd.read_csv('billions.csv')

# Distribuição de Fontes de Riqueza
fontes_riqueza = data[data['country'] == 'Brazil'].groupby(
    'source').size().sort_values(ascending=False)
print("Distribuição de Fontes de Riqueza no Brasil:")
print(fontes_riqueza)
print("\n")

# Relação entre Educação e Riqueza
media_educacao_brasil = data[data['country'] ==
                             'Brazil']['gross_tertiary_education_enrollment'].mean()
media_educacao_global = data['gross_tertiary_education_enrollment'].mean()
print(
    f"Média da taxa de matrícula em educação terciária no Brasil: {media_educacao_brasil:.2f}")
print(
    f"Média da taxa de matrícula em educação terciária global: {media_educacao_global:.2f}")
print("\n")

# Impostos e Riqueza
media_impostos_brasil = data[data['country'] ==
                             'Brazil']['tax_revenue_country_country'].mean()
top10_paises_bilionarios = data.groupby(
    'country').size().sort_values(ascending=False).head(10).index
media_impostos_top10 = data[data['country'].isin(
    top10_paises_bilionarios)]['tax_revenue_country_country'].mean()
print(f"Média da receita fiscal no Brasil: {media_impostos_brasil:.2f}")
print(
    f"Média da receita fiscal nos 10 países com mais bilionários: {media_impostos_top10:.2f}")
print("\n")

# Análise de Gênero
genero_brasil = data[data['country'] ==
                     'Brazil']['gender'].value_counts(normalize=True) * 100
genero_global = data['gender'].value_counts(normalize=True) * 100
print("Proporção de bilionários por gênero no Brasil:")
print(genero_brasil)
print("Proporção de bilionários por gênero no mundo:")
print(genero_global)
print("\n")

# Localização dos Bilionários
cidades_bilionarios = data[data['country'] == 'Brazil']['city'].value_counts()
print("Principais cidades no Brasil onde residem os bilionários: ")
print(cidades_bilionarios)
print("\n")

# Análise da Longevidade e Riqueza
expectativa_vida_brasil = data[data['country']
                               == 'Brazil']['life_expectancy_country'].mean()
top10_paises_ricos = data.sort_values('finalWorth', ascending=False).head(10)[
    'country'].unique()
expectativa_vida_top10 = data[data['country'].isin(
    top10_paises_ricos)]['life_expectancy_country'].mean()
print(f"Expectativa de vida média no Brasil: {expectativa_vida_brasil:.2f}")
print(
    f"Expectativa de vida média nos países dos 10 bilionários mais ricos do mundo: {expectativa_vida_top10:.2f}")

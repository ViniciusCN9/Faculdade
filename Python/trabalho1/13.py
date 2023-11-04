import json


def ler_json(nome_arquivo):
    try:
        with open(nome_arquivo, 'r') as arquivo:
            dados = json.load(arquivo)
            return dados
    except IOError:
        print(f"Erro ao ler o arquivo '{nome_arquivo}'")
        return None


arquivo_json = 'dados_paises.json'

dados_carregados = ler_json(arquivo_json)

if dados_carregados:
    print("Dicionário carregado do arquivo JSON:")
    print(dados_carregados)

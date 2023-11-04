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

    dados_carregados['Brasil']['População'] = 220000000
    dados_carregados['Argentina'] = {
        'Capital': 'Buenos Aires', 'População': 45000000, 'Idioma': 'Espanhol'}

    def salvar_json(dados, nome_arquivo):
        try:
            with open(nome_arquivo, 'w') as arquivo:
                json.dump(dados, arquivo, indent=4)
            print(f"Dados salvos com sucesso no arquivo '{nome_arquivo}'")
        except IOError:
            print(f"Erro ao escrever no arquivo '{nome_arquivo}'")

    salvar_json(dados_carregados, arquivo_json)

import json

informacoes_paises = {
    'Brasil': {
        'Capital': 'Brasília',
        'População': 213993437,
        'Idioma': 'Português'
    },
    'Estados Unidos': {
        'Capital': 'Washington, D.C.',
        'População': 331449281,
        'Idioma': 'Inglês'
    },
    'França': {
        'Capital': 'Paris',
        'População': 65273511,
        'Idioma': 'Francês'
    }
}


def salvar_json(dados, nome_arquivo):
    try:
        with open(nome_arquivo, 'w') as arquivo:
            json.dump(dados, arquivo, indent=4)
        print(f"Dados salvos com sucesso no arquivo '{nome_arquivo}'")
    except IOError:
        print(f"Erro ao escrever no arquivo '{nome_arquivo}'")


salvar_json(informacoes_paises, 'dados_paises.json')

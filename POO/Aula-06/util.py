def ajusteData(data : str):
    dia = data.split('/')[0]
    mes = data.split('/')[1]
    ano = data.split('/')[2]

    return f'{ano}-{mes}-{dia}'
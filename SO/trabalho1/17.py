import os

caminho = "minhapasta"

if os.path.exists(caminho) and os.path.isdir(caminho):
    conteudo_minhapasta = os.listdir(caminho)

    for item in conteudo_minhapasta:
        print(item)
else:
    print("O diretório 'minhapasta' não existe ou não é uma pasta.")

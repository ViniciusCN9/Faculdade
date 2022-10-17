import os
import pathlib

caminho = "./arquivos"
arquivos = os.listdir(caminho)
imagens = [arquivo for arquivo in arquivos if arquivo.lower().endswith(".jpg") or arquivo.lower().endswith(".webp")]

# print(imagens)

for arquivo in arquivos:
    path = pathlib.PurePath(arquivo)
    print(path.suffix)

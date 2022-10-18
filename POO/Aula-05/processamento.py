import os
import numpy as np
import cv2

def criarDiretorio(path):
    diretorio = f"{path.removesuffix('.jpg')}img"
    if not os.path.isdir(diretorio):
        os.mkdir(diretorio)

def processar(path, pasta):
    imagem = cv2.imread(path)
    altura = imagem.shape[0]
    largura = imagem.shape[1]
    canal =imagem.shape[2]

    criarDiretorio(path)

    vermelho = np.zeros([altura, largura, 3], dtype=np.uint8)
    verde = np.zeros([altura, largura, 3], dtype=np.uint8)
    azul =  np.zeros([altura, largura, 3], dtype=np.uint8)

    for i in range(altura):
        for j in range(largura):
            pixel = imagem[i, j]
            r = pixel[2]
            g = pixel[1]
            b = pixel[0]

            vermelho[i, j] =[0,0,r]
            verde[i, j] =[0,g,0]
            azul[i, j] =[b,0,0]
            
    cv2.imwrite(os.path.join(path, pasta, "vermelho.png"), vermelho)
    cv2.imwrite(os.path.join(path, pasta, "verde.png"), verde)
    cv2.imwrite(os.path.join(path, pasta, "azul.png"), azul)

caminho = "./imagens"
arquivos = os.listdir(caminho)

for arquivo in arquivos:
    path = os.path.join(caminho, arquivo)
    processar(path, f"{arquivo.removesuffix('.jpg')}img")
    
    


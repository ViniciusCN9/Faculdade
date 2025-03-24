import os

if os.path.exists("meuarquivo.txt") and os.path.isfile("meuarquivo.txt"):
    print("O arquivo 'meuarquivo.txt' existe no diretório atual.")
else:
    print("O arquivo 'meuarquivo.txt' não foi encontrado no diretório atual.")

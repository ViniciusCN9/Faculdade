import os

if os.path.exists("copia_meuarquivo.txt"):
    os.rename("copia_meuarquivo.txt", "renomeado.txt")
    print("Arquivo renomeado com sucesso!")
else:
    print("O arquivo 'copia_meuarquivo.txt' não existe.")

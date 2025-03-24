import os

if os.path.exists("renomeado.txt"):
    os.remove("renomeado.txt")
    print("Arquivo 'renomeado.txt' excluído com sucesso!")
else:
    print("O arquivo 'renomeado.txt' não existe.")

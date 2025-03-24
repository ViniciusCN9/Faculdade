import os

if not os.path.exists("minhapasta"):
    os.mkdir("minhapasta")
    print("Pasta 'minhapasta' criada com sucesso!")
else:
    print("A pasta 'minhapasta' já existe.")

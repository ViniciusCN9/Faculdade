PATH = "dados.txt"

nomes = []

arquivo = open(PATH, "r")
linhas = arquivo.readlines()

for linha in linhas:
    nomes.append(linha.removesuffix("\n"))

arquivo.close()

print(nomes)
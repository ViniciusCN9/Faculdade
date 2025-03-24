import csv

dados = [
    ["Nome", "Idade", "Endereço"],
    ["Alice", 30, "Rua A"],
    ["Bob", 25, "Rua B"],
    ["Carol", 35, "Rua C"]
]

with open("dados.csv", mode="w", newline="") as arquivo_csv:
    escritor_csv = csv.writer(arquivo_csv)
    escritor_csv.writerows(dados)

print("Arquivo 'dados.csv' criado com sucesso.")

from faker import Faker
fake = Faker()

PATH = "dados.txt"
QUANTIDADE = 100

arquivo = open(PATH, "w")

for i in range(QUANTIDADE):
    nome = fake.name()
    email = f'{nome.lower().replace(" ", "")}@{fake.free_email().split("@")[1]}'

    dado = f"nome: {nome} | email: {email}\n"
    
    if i == (QUANTIDADE - 1):
        arquivo.write(dado.removesuffix("\n"))
    else:
        arquivo.write(dado)
    
arquivo.close()

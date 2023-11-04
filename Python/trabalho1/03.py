estoque = {
    "geladeira": 10,
    "fogão": 15,
    "tv": 9,
    "batedeira": 5,
    "ventilador": 22
}

for nome, quantidade in estoque.items():
    if (quantidade > 10):
        print(nome)

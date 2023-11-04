estoque = {
    "geladeira": 10,
    "fogão": 15,
    "tv": 9,
    "batedeira": 5,
    "ventilador": 22
}


def adiciona_estoque(nome, quantidade):
    if nome in estoque:
        estoque[nome] += quantidade
        return
    estoque[nome] = quantidade


adiciona_estoque("ventilador", 5)
adiciona_estoque("tv", 2)
adiciona_estoque("video-game", 15)
adiciona_estoque("caderno", 3)
print(estoque)

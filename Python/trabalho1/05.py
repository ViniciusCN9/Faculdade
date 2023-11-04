biblioteca = {
    "livroA": {
        "autor": "autorA",
        "ano": 2020,
        "genero": "generoA"
    },
    "livroB": {
        "autor": "autorB",
        "ano": 2021,
        "genero": "generoA"
    },
    "livroC": {
        "autor": "autorC",
        "ano": 2022,
        "genero": "generoC"
    },
    "livroD": {
        "autor": "autorC",
        "ano": 2023,
        "genero": "generoC"
    }
}


def buscar_por_autor(autor):
    titulos = []
    for titulo, informacao in biblioteca.items():
        if informacao["autor"] == autor:
            titulos.append(titulo)
    return titulos


print(buscar_por_autor("autorA"))
print(buscar_por_autor("autorB"))
print(buscar_por_autor("autorC"))

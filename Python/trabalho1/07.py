def contar_frutas(lista):
    contagem_frutas = {}
    for fruta in lista:
        contagem_frutas[fruta] = contagem_frutas.get(fruta, 0) + 1
    return contagem_frutas


frutas = ['maçã', 'banana', 'maçã', 'laranja',
          'banana', 'maçã', 'uva', 'laranja']
resultado = contar_frutas(frutas)
print(resultado)

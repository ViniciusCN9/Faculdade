def calcularAreaQuadrado(lado):
    print(f"A área do quadrado é de {lado ** 2}")

def calcularAreaQuadradoComRetorno(lado):
    return lado ** 2

def	dados(nome,	idade=None):
    print(f'nome: {nome}')
    if(idade is not None):
        print(f'idade: {idade}')
    else:
        print('idade: não informada')

def	dadosComRetorno(nome, idade=None):
    if(idade is not None):
        return (f'nome: {nome} \nidade: {idade}')
    else:
        return (f'nome: {nome} \nidade: não informada')

def	calculadora(x, y):
	return	{'soma':x + y,	'subtração': x - y, 'multiplicação': x * y}

def	teste(arg,	*args):
	print(f'primeiro argumento normal: {arg}')
	for	arg	in args:
		print(f'outro argumento: {arg}')
        
calcularAreaQuadrado(10)
area = calcularAreaQuadradoComRetorno(10)
print(f"A área do quadrado é de {area}")

dados('João')
dados('Maria', 32)

print(dadosComRetorno('João'))
print(dadosComRetorno('Maria', 32))

resultados = calculadora(1,	2)
for	chave in resultados:
    print(f'{chave}: {resultados[chave]}')
				
teste('python', 'é', 'muito', 'legal')
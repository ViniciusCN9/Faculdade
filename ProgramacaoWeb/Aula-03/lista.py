import os

notas = []
soma = 0

def validaValor(tipo, mensagem):
    while True:
        try:
            match tipo:
                case "int":
                    valor = int(input(mensagem))
                    return valor
                case "float":
                    valor = float(input(mensagem))
                    return valor
        except:
            print("Insira um valor válido")

quantidadeNotas = validaValor("int", "Insira a quantidade de notas: ")

for i in range(0, quantidadeNotas):
    nota = 0
    
    while True:
        nota = validaValor("float", f"Insira a {i + 1}º nota: ")
        if (nota >= 0 and nota <= 10):
            break

        print("Nota inválida!")
        
    notas.append(nota)
    soma += nota

print(f"A(s) {quantidadeNotas} nota(s) inserida(s) foram: {notas}")
print("A médias das notas é de: %2.2f" % (soma/quantidadeNotas))



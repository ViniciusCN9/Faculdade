notas = []
numero_alunos = int(input("Digite o número de alunos: "))

for i in range(numero_alunos):
    nota = float(input(f"Digite a nota do aluno {i + 1}: "))
    notas.append(nota)

media = sum(notas) / len(notas)
nota_maxima = max(notas)
nota_minima = min(notas)

print(f"Média das notas: {media:.2f}")
print(f"Maior nota: {nota_maxima}")
print(f"Menor nota: {nota_minima}")
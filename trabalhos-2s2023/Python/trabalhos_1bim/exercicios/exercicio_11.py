alunos_notas = [("João", (8, 7, 9)), ("Maria", (9, 9, 8)), ("Carlos", (7, 6, 7))]

for aluno, notas in alunos_notas:
    media = sum(notas) / len(notas)
    print(f"{aluno}: Média = {media:.2f}")
    
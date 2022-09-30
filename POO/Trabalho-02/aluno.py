class aluno():
    id = 1
    def __init__(self, nome, curso):
        self.id = aluno.id
        self.nome = nome
        self.curso = curso

        aluno.id += 1


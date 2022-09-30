class Aluno():
    id = 1
    def __init__(self, nome, curso):
        self.id = Aluno.id
        self.nome = nome
        self.curso = curso

        Aluno.id += 1


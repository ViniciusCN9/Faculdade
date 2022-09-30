from cursoEnum import curso

class faculdade():
    def __init__(self):
        self.nome = "Faculdade Gran-Tietê"
        self.alunos = []
        self.cursos = [curso.ENGENHARIA_MECANICA, curso.ENGENHARIA_COMPUTACAO, curso.ENGENHARIA_PRODUCAO]

    def listarAlunos(self):
        for aluno in self.alunos:
            print(f"Nome do aluno: {aluno.nome} | Curso do aluno: {aluno.curso}")

    def listarAluno(self, id):
        for aluno in self.alunos:
            if (aluno.id == id):
                print(f"Nome do aluno: {aluno.nome} | Curso do aluno: {aluno.curso}")

    def adicionarAluno(self, aluno):
        self.alunos.append(aluno)

    def removerAluno(self, id):
        for aluno in self.alunos:
            if (aluno.id == id):
                self.alunos.pop(aluno)

    def atualizarAluno(self, id, nome, curso):
        for aluno in self.alunos:
            if (aluno.id == id):
                aluno.nome = nome
                aluno.curso = curso

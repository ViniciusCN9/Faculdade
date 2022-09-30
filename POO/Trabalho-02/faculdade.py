from curso import Curso

class Faculdade():
    nome = "Faculdade Gran-Tietê"
    alunos = []
    cursos = [Curso.ENGENHARIA_MECANICA, Curso.ENGENHARIA_COMPUTACAO, Curso.ENGENHARIA_PRODUCAO]

    def listarAlunos():
        if (len(Faculdade.alunos) == 0):
            print("Nenhum aluno cadastrado")

        for aluno in Faculdade.alunos:
            print(f"Id: {aluno.id} | Nome do aluno: {aluno.nome} | Curso do aluno: {aluno.curso}")

    def listarAluno(id):
        for aluno in Faculdade.alunos:
            if (aluno.id == id):
                print(f"Id: {aluno.id} | Nome do aluno: {aluno.nome} | Curso do aluno: {aluno.curso}")
            else:
                print("Aluno não encontrado!")

    def adicionarAluno(aluno):
        Faculdade.alunos.append(aluno)

    def removerAluno(id):
        for aluno in Faculdade.alunos:
            if (aluno.id == id):
                Faculdade.alunos.pop(aluno)

    def atualizarAluno(id, nome, curso):
        for aluno in Faculdade.alunos:
            if (aluno.id == id):
                aluno.nome = nome
                aluno.curso = curso

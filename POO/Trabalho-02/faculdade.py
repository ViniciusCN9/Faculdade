class Faculdade():
    nome = "Faculdade Gran-Tietê"
    alunos = []
    cursos = {}

    def listarAlunos():
        if (len(Faculdade.alunos) == 0):
            print("Nenhum aluno cadastrado!")
            return

        for aluno in Faculdade.alunos:
            print(f"Id: {aluno.id} | Nome do aluno: {aluno.nome} | Curso do aluno: {aluno.curso.name}")

    def listarAluno(id):
        try:
            aluno = next((aluno for aluno in Faculdade.alunos if aluno.id == id))
            print(f"Id: {aluno.id} | Nome do aluno: {aluno.nome} | Curso do aluno: {aluno.curso.name}")
            return aluno
        except:
            print("Aluno não encontrado!")
            return False

    def adicionarAluno(aluno):
        Faculdade.alunos.append(aluno)

    def atualizarAluno(id, nome, curso):
        try:
            aluno = next((aluno for aluno in Faculdade.alunos if aluno.id == id))
            aluno.nome = nome
            aluno.curso = curso
        except:
            print("Aluno não encontrado!")

    def removerAluno(id):
        try:
            aluno = next((aluno for aluno in Faculdade.alunos if aluno.id == id))
        except:
            print("Aluno não encontrado!")
            return False

        Faculdade.alunos.remove(aluno)

    def listarCursos():
        print("Cursos disponíveis: ")
        for key, value in Faculdade.cursos.items():
            print(f"Id: {key} | Curso: {value}")


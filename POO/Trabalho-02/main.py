from tela import carregando, opcoes, encerrando
from faculdade import Faculdade
from curso import Curso
from aluno import Aluno

def main():
    carregando()
    opcoes()
    encerrando()

# Adicionando alguns cursos à faculdade
Faculdade.cursos.update({
    Curso.ENGENHARIA_MECANICA.value : Curso.ENGENHARIA_MECANICA.name, 
    Curso.ENGENHARIA_COMPUTACAO.value : Curso.ENGENHARIA_COMPUTACAO.name, 
    Curso.ENGENHARIA_PRODUCAO.value : Curso.ENGENHARIA_PRODUCAO.name,
    Curso.ENFERMAGEM.value : Curso.ENFERMAGEM.name,
    Curso.NUTRICAO.value : Curso.NUTRICAO.name
})

# Adicionando alguns alunos à faculdade
Faculdade.adicionarAluno(Aluno("Pedro Miguel Pires", Curso.ENFERMAGEM))
Faculdade.adicionarAluno(Aluno("Maria Clara Sales", Curso.ENGENHARIA_COMPUTACAO))
Faculdade.adicionarAluno(Aluno("Lara Nunes", Curso.ENGENHARIA_PRODUCAO))
Faculdade.adicionarAluno(Aluno("Carlos Eduardo Costa", Curso.NUTRICAO))
Faculdade.adicionarAluno(Aluno("Evelyn Monteiro", Curso.ENFERMAGEM))
Faculdade.adicionarAluno(Aluno("Bruno Ramos", Curso.ENGENHARIA_MECANICA))
Faculdade.adicionarAluno(Aluno("Cauã Teixeira", Curso.ENGENHARIA_COMPUTACAO))
Faculdade.adicionarAluno(Aluno("Eduardo Dias", Curso.ENGENHARIA_PRODUCAO))
Faculdade.adicionarAluno(Aluno("Camila Duarte", Curso.NUTRICAO))
Faculdade.adicionarAluno(Aluno("Pedro Gomes", Curso.ENGENHARIA_MECANICA))

main()
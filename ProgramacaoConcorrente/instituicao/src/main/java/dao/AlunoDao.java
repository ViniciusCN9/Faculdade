package dao;

import java.util.ArrayList;
import java.util.List;
import java.util.Optional;

import models.Aluno;

public class AlunoDao {
	
	public static List<Aluno> alunos = new ArrayList<Aluno>();
	
	public List<Aluno> getAlunos() {
		return alunos;
	}
	
	public Aluno getAluno(int id) {
		Optional<Aluno> aluno = alunos.stream().filter(e -> e.getId() == id).findFirst();
		return aluno.get();
	}
	
	public void insertAluno(String nome) {
		alunos.add(new Aluno(nome));
	}
	
	public void updateAluno(int id, String nome) {
		Optional<Aluno> aluno = alunos.stream().filter(e -> e.getId() == id).findFirst();
		aluno.ifPresent(e -> {e.setNome(nome); alunos.set(alunos.indexOf(aluno.get()), e);});
	}
	
	public void removeAluno(int id) {
		Optional<Aluno> aluno = alunos.stream().filter(e -> e.getId() == id).findFirst();
		aluno.ifPresent(e -> alunos.remove(e));
	}
}

package connections;

import java.util.ArrayList;
import java.util.List;
import models.Aluno;

public class DatabaseConnection {
	
	public List<Aluno> Alunos;
	
	public DatabaseConnection() {
		this.Alunos = new ArrayList<Aluno>();
		this.Alunos.add(new Aluno("João"));
		this.Alunos.add(new Aluno("Maria"));
		this.Alunos.add(new Aluno("Pedro"));
	}
	
	public List<Aluno> getAlunos() {
		return this.Alunos;
	}
	
	public Aluno getAluno(int id) {
		for (Aluno aluno : this.Alunos) {
			if (aluno.Id == id) {
				return aluno;
			}
		}
		return null;
	}
	
	public void insertAluno(String nome) {
		this.Alunos.add(new Aluno(nome));
	}
	
	public void updateAluno(int id, String nome) {
		for (Aluno aluno : this.Alunos) {
			if (aluno.Id == id) {
				aluno.Nome = nome;
			}
		}
		
	}
	
	public void removeAluno(int id) {
		for (Aluno aluno : this.Alunos) {
			if (aluno.Id == id) {
				this.Alunos.remove(aluno);
			}
		}
	}
}

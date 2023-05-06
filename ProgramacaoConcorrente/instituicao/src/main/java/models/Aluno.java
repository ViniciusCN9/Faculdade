package models;

public class Aluno {
	
	private static int ID_COUNTER = 1;
	private int Id;
	private String Nome;
	
	public Aluno(String nome) {
		this.Id = ID_COUNTER;
		this.Nome = nome;
		
		ID_COUNTER++; 
	}
	
	public int getId() {
		return this.Id;
	}

	public String getNome() {
		return this.Nome;
	}
	
	public void setNome(String nome) {
		this.Nome = nome;
	}
}

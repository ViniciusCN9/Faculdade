package models;

public class Aluno {
	
	private static int ID_COUNTER = 1;
	public int Id;
	public String Nome;
	
	public Aluno(String nome) {
		Id = ID_COUNTER;
		Nome = nome;
		
		ID_COUNTER++; 
	}
	
	public int getId() {
		return Id;
	}
	public void setId(int id) {
		Id = id;
	}
	public String getNome() {
		return Nome;
	}
	public void setNome(String nome) {
		Nome = nome;
	}
}
